import re
import sys
import time
import click
from os.path import expanduser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from progress.bar import IncrementalBar

def getUserDocumentPath():
	"""Locate Personal User document folder
	Returns:
		[string] -- Return destanation download path
	"""
	return expanduser("~") + "/Documents/icons/"

def collectionName(url):
	"""Split URL and get collection name
	Arguments:
		url {[string]} -- URL of SVGREPO Collection
	Returns:
		[string] -- Collection Name
	"""
	url_splited = url.split('/')
	url_splited = [i for i in url_splited if i]
	return url_splited.pop()

def downloader(url, path):
	urlChecker(url)
	dest = path + collectionName(url)
	click.echo('📣 Download will start for %s pack !' % collectionName(url))
	driver = browserConfiguration(dest)
	runBrowser(driver, url)

def browserConfiguration(path):
	"""Configure selenium browser
	Run headless firefox and configure download path
	
	Arguments:
		path {[string]} -- Destination download path
	Returns:
		[object] -- Firefox Webdriver
	"""
	profile = FirefoxProfile()
	profile.set_preference("browser.download.panel.shown", False)
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.dir", path)
	options = Options()
	options.add_argument("--headless")
	return webdriver.Firefox(firefox_profile=profile, options=options)

def urlChecker(url):
	"""Check url
	Regex check if given by user equal to svgrepo collection
	
	Arguments:
		url {[type]} -- [description]
	"""
	pattern =  '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)[a-z0-9]+([\-\.]svgrepo+)\.[a-z]{2,5}(\/collection\/)([a-zA-Z0-9-_]+)/?$'
	result = re.match(pattern,url)
	if not result:
		click.echo('😱 Oups URL provided not match !')
		click.echo('💡 Your URL should look like this : https://svgrepo/collection/[id]')
		sys.exit()

# @TODO=use WebDriverWait and find_elements_by_*
def runBrowser(driver, url):
	"""Run browser and start dowload
	Run browser and start download with progress bar
	
	Arguments:
		driver {[object]} -- Browser 
		url {[string]} -- URL of SVGREPO Collection
	"""
	driver.get(url)
	time.sleep(3) #REACT app need to sleep and wait app load.
	all_links=driver.execute_script('all_links = []; links = document.querySelectorAll(".style-module--action--1Avvt>a"); links.forEach(url => all_links.push(url.href)); return all_links');
	bar = IncrementalBar('📥 Icons Downloaded', max = len(all_links))
	
	for i, link in  enumerate(all_links):
		driver.execute_script('''window.open("'''+link+'''","_blank");''')
		bar.next()
	driver.close()
	click.echo('\n🎉 Download done!')
	click.echo('🙏 Thanks for using svgrepodl!')