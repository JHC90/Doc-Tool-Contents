# call:
# python .\00_basicWebsiteAvailiblity.py https://www.google.de
from selenium import webdriver
import sys
import time
url = sys.argv[1]

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1
)
driver.close()