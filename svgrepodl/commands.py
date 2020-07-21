import click
from .utils import getUserDocumentPath, downloader
from .HttpStatusCode import HttpStatusCode

@click.command()
@click.option('--path', '-p', default=getUserDocumentPath(), help="Change download destination path.")
@click.argument('url')
def cli(path, url):
	"""Run Command
	Run downloader to get SVGREPO pack
	
	Decorators:
		click.command
		click.option
		click.argument
	Arguments:
		path {[string]} -- Destination download path
		url {[string]} -- URL of SVGREPO Collection
	"""
	urlResponseChecker = HttpStatusCode(url).httpGetResponse() 
	if(urlResponseChecker != 404):
		downloader(url, path)
	else:
		click.echo("😱 Cannot get this URL!")