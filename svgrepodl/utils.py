import os
import time
from .Message import Message
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from progress.bar import IncrementalBar

def downloader(url, path):
	driver = browserConfiguration(path)
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
	return webdriver.Firefox(firefox_profile=profile, options=options, service_log_path=os.path.devnull)

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
	print('\n')
	driver.close()
	Message.success('🎉 Download done!')