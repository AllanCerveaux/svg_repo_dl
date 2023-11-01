import sys
import re
import os
import requests
import bs4
from .Message import Message
from progress.bar import IncrementalBar


class DownloadException(Exception):
    pass


def get_page(soup):
    page_footer = soup.select('div[class^="style_pagingCarrier"]')[0].get_text()
    return int(re.sub(r'.*/\s+', r'', page_footer))


def list_collections(category='all'):
    url = f'https://www.svgrepo.com/collections/{category}/'
    page1 = requests.get(url)
    if page1.status_code != 200:
        raise DownloadException()
    soup = bs4.BeautifulSoup(page1.text, features="lxml")
    num_page = get_page(soup)
    for page in range(1, int(num_page) + 1):
        print(f'page {page}/{num_page}', file=sys.stderr)
        if page > 1:
            html = requests.get(url + str(page))
            soup = bs4.BeautifulSoup(html.text, features="lxml")
        all_links = soup.select('div[class^="style_Collection__"] a')
        all_links = [a.get('href') for a in all_links]
        print("\n".join(all_links))


def downloader(url, path):
    """
    Download a collection (or a search)

    Arguments:
    url {[string]} -- URL of SVGREPO Collection
    """
    is_search = '/vectors/' in url
    page1 = requests.get(url)
    if page1.status_code != 200:
        raise DownloadException()
    soup = bs4.BeautifulSoup(page1.text, features="lxml")

    os.makedirs(path, exist_ok=True)
    num_page = 99 if is_search else get_page(soup)
    for page in range(1, int(num_page) + 1):
        if page > 1:
            html = requests.get(url + str(page))
            soup = bs4.BeautifulSoup(html.text, features="lxml")
        all_links = soup.select('div[class^="style_NodeImage_"] img[itemprop="contentUrl"]')
        all_links = [a.get('src') for a in all_links]
        if len(all_links) == 0:
            break

        bar = IncrementalBar('📥 Icons URLs page %d/%d' % (page, num_page), max=len(all_links))
        for link in all_links:
            aid = os.path.basename(os.path.dirname(link))
            dest = os.path.join(path, aid + '-' + os.path.basename(link))
            if os.path.exists(dest):
                # print("already exists", link, file=sys.stderr)
                continue
            x = requests.get(link)
            if x.headers.get('content-type') != 'image/svg+xml':
                print("err", link, file=sys.stderr)
                continue
            with open(dest, 'wb') as f:
                f.write(x.content)
            bar.next()
        bar.finish()

    Message.success('🎉 Finished')
