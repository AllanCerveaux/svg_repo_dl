import sys
import click
from .Url import Url
from .utils import getUserDocumentPath, downloader

@click.command()
@click.option('--path', '-p', default=getUserDocumentPath(), help="Change download destination path.")
@click.argument('url')
def cli(path, url):
	"""Run downloader to get SVGREPO pack
	
	Decorators:
		click.command
		click.option
		click.argument
	Arguments:
		path {[string]} -- Destination download path
		url {[string]} -- URL of SVGREPO Collection
	"""
	url = Url(url) 
	if not url.checker():
		click.echo('😱 Oups URL provided not match !')
		click.echo('💡 Your URL should look like this : https://svgrepo/collection/[id]')
		sys.exit()

	if(url.httpGetResponse() != 404):
		downloader(url, path)
	else:
		click.echo("😱 Cannot get this URL!")
		sys.exit()