# call:
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python .\01_basicWebsiteinteractive.py file:///C:/DocTool/output/index.html
# Ziel ist es unterschiedliche Websiten aufzurufen und von dort aus die Navigationsleiste immer auf die gleiche Art zu testetn
# Die navigation wurde inital einmalig erstellt und 
from selenium import webdriver
import sys
import time
url = sys.argv[1]

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)
navField = driver.find_element_by_name('about')
navField.click()

time.sleep(2)
navField = driver.find_element_by_name('index')
navField.click()

time.sleep(2)
navField = driver.find_element_by_name('Docus')
navField.click()

time.sleep(2)
navField = driver.find_element_by_name('Projekte')
navField.click()



time.sleep(2)
driver.close()
