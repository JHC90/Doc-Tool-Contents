# call:
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python 01_navBarTesting-Basic.py file:///C:/DocTool/output/index.html
# Ziel ist es unterschiedliche Webpages aufgerufen werden. Die Navbar müsste eigentlich immer gleich implementiert sein.
# Es ist also egal ob ich von der \index.html die .\about,html aufrufe od ero bich ausgehend von Docus\Programmoerien\Python.html die Seite .\aboutt aufrufe.
# und von dort aus die Navigationsleiste immer auf die gleiche Art zu testetn
# Die navigation wurde inital einmalig erstellt und wurde in alle nachgelagerten Webpages idetnisch implementiert.
from selenium import webdriver
import sys
import time
url = sys.argv[1]

driver = webdriver.Chrome()
driver.get(url)

error = ""

# Multilevel
try:
    time.sleep(2)
    navField = driver.find_element_by_name('Docus')
    navField.click()
    navField = driver.find_element_by_name('Informatik')
    navField.click()
    navField = driver.find_element_by_name('Programmieren')
    navField.click()
    navField = driver.find_element_by_name('Python')
    navField.click()
    navField = driver.find_element_by_name('Bibliotheken')
    navField.click()
    navField = driver.find_element_by_name('Selenium')
    navField.click()
    navField = driver.find_element_by_name('testfile')
    navField.click()

# Level 2
time.sleep(2)
navField = driver.find_element_by_name('Docus')
navField.click()
navField = driver.find_element_by_name('Mathe')
navField.click()
navField = driver.find_element_by_name('Mathe-BigPicture')
navField.click()

# Level 1

time.sleep(2)
navField = driver.find_element_by_name('index')
navField.click()

time.sleep(2)
navField = driver.find_element_by_name('about')
navField.click()

time.sleep(2)
navField = driver.find_element_by_name('Docus')
navField.click()

time.sleep(2)
navField = driver.find_element_by_name('Projekte')
navField.click()

time.sleep(2)
driver.close()