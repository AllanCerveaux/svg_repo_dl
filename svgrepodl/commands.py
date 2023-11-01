import os
import sys
import re
import click
from .Url import Url
from .Message import Message
from .utils import downloader, DownloadException

@click.command()
@click.option('--path', '-p', default=os.getcwd(), help="Destination path.")
@click.argument('urls', nargs=-1)
def cli(path, urls):
    """Run downloader to get SVGREPO pack

    Decorators:
        click.command
        click.option
        click.argument
    Arguments:
        path {[string]} -- Destination download path
        url {[string]} -- URL of SVGREPO Collection
    """

    path = os.path.realpath(os.path.expanduser(path))
    for i, url in enumerate(urls):
        url = url.rstrip('/') + '/'
        urlHelpers = Url(url)
        if not urlHelpers.checker():
            Message.error('😱 Specified URL unsupported')
            Message.info('💡 URL should look like "https://svgrepo.com/collection/[id]"')
            continue

        is_search = '/vectors/' in url
        if is_search:
            term = re.match(r'.*/vectors/([^/?#&]+)', url).group(1)
            dest = os.path.join(path, 'search', term)
            Message.info(f'📣 Download {i}/{len(urls)}: Search results for "{term}"')
        else:
            collection = urlHelpers.collectionName()
            dest = os.path.join(path, collection)
            Message.info(f'📣 Download {i}/{len(urls)}: Collection {collection}')

        try:
            downloader(url, dest)
        except DownloadException:
            Message.error(f"😱 Cannot get this URL {url}!")
