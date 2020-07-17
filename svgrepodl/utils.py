import re
import sys
import time
import click
from os.path import expanduser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from progress.bar import IncrementalBar

# Get Documents User path and make folder icons.
def getUserDocumentPath():
	return expanduser("~") + "/Documents/icons/"

def collectionName(url):
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
	pattern = '^(?:https?://www\.svgrepo\.com(?:/\S*)*|sc-domain:www\.svgrepo\.com)$'
	result = re.match(pattern, url)
	if result:
		pass
	else:
		click.echo('This is not the url of SVGREPO go to this address to download icons: https://www.svgrepo.com/')
		sys.exit()

# @TODO=use WebDriverWait and find_elements_by_*
def runBrowser(driver, url):
	driver.get(url)
	time.sleep(3)
	all_links=driver.execute_script('all_links = []; links = document.querySelectorAll(".style-module--action--1Avvt>a"); links.forEach(url => all_links.push(url.href)); return all_links');
	bar = IncrementalBar('📥 Icons Downloaded', max = len(all_links))
	
	for i, link in  enumerate(all_links):
		driver.execute_script('''window.open("'''+link+'''","_blank");''')
		bar.next()
	driver.close()
	click.echo('\n🎉Download done !')