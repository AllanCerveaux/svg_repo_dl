import sys
import re
import os
import requests
import bs4
from .Message import Message
from progress.bar import IncrementalBar


class DownloadException(Exception):
    pass


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
    if is_search:
        num_page = 99
    else:
        page_footer = soup.select('div[class^="style_pagingCarrier"]')[0].get_text()
        num_page = int(re.sub(r'.*/\s+', r'', page_footer))

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

    print('\n')
    Message.success('🎉 Finished')
