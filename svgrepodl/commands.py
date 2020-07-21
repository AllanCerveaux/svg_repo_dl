import sys
import click
from .Url import Url
from .Message import Message
from .utils import downloader
from os.path import expanduser

def getUserDocumentPath():
	"""Locate Personal User document folder
	Returns:
		[string] -- Return destanation download path
	"""
	return expanduser("~") + "/Documents/icons/"

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
	urlHelpers = Url(url) 
	if not urlHelpers.checker():
		Message.error('😱 Oups URL provided not match !')
		Message.info('💡 Your URL should look like this : https://svgrepo/collection/[id]')
		sys.exit()

	if(urlHelpers.httpGetResponse() != 404):
		dest = path + urlHelpers.collectionName();
		Message.info('📣 Download will start for %s pack !' % urlHelpers.collectionName())
		downloader(url, dest)
	else:
		Message.error("😱 Cannot get this URL!")
		sys.exit()