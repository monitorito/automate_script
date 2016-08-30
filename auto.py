from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import sys, getopt

def switchToTab(web_driver, num):
	web_driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + str(num+1))
	web_driver.switch_to_window(web_driver.window_handles[num])

def createNewTab(web_driver):
	body = web_driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

def usage():
	print 'Usage:'
	print 'auto.py -i <inputfile>'

def main(argv, chromeBinaryLocation, chromeUserDataDirectory, extensionID, mode):
	inputFileProvided = False
	try:
		opts, args = getopt.getopt(argv,"hi:", ["input="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("-i", "--input"):
			inputFileProvided = True
			inputFile = arg

	if not inputFileProvided:
		usage()
		sys.exit()

	opts = Options()
	opts.binary_location = chromeBinaryLocation
	opts.add_argument("user-data-dir=" + chromeUserDataDirectory)
	driver = webdriver.Chrome(chrome_options=opts)
	driver.set_page_load_timeout(5)

	driver.get("chrome-extension://" + extensionID + "/index.html")
	if mode == "offline": 
		driver.find_element_by_id("offline-mode").click()
	elif mode == "online":
		driver.find_element_by_id("online-mode").click()
	else:
		print "Invalid value for mode. It must be either 'offline' or 'online'."
		sys.exit()

	createNewTab(driver)
	switchToTab(driver, 1)

	file = open(inputFile, 'r')
	for line in file:
		url = line.strip()
		try:
			driver.get(url)
			switchToTab(driver, 0)
			time.sleep(0.1)
			switchToTab(driver, 1)
		except TimeoutException:
			print(url, " interrupted while loading")
		
	#prevent browser from closing to extract data
	time.sleep(1000)

	switchToTab(driver, 0)
	wait = WebDriverWait(driver, 1)


if __name__ == "__main__":
	#Extension mode ["online", "offline"]
	mode = "offline"
	#Environment Parameters
	chromeBinaryLocation = "/opt/google/chrome/google-chrome"
	chromeUserDataDirectory = "/home/user/.config/google-chrome"
	extensionID = "obleabjcolndljhmdbnknkdjgkmoodpe"

	main(sys.argv[1:], chromeBinaryLocation, chromeUserDataDirectory, extensionID, mode)