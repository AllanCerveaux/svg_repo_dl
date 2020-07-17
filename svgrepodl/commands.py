import click
from .utils import getUserDocumentPath, downloader

@click.command()
@click.option('--path', '-p', default=getUserDocumentPath(), help="Change download destination path.")
@click.argument('url')
def cli(path, url):
	downloader(url, path)