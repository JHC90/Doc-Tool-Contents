# call:
# python .\01_basicWebsiteinteractive.py file:///C:/DocTool/output/index.html
from selenium import webdriver
import sys
import time
url = sys.argv[1]

driver = webdriver.Chrome()
driver.get(url)


driver.close()
