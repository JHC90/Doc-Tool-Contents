# call:
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python 01_navBarTesting-Basic.py file:///C:/DocTool/output/index.html "['index', 'about']"
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python 01_navBarTesting-Basic.py file:///C:/DocTool/output/index.html "['index', 'about', 'Docus', 'Projekte', ['Docus', 'DataScience']]"




# Ziel ist es unterschiedliche Webpages aufgerufen werden. Die Navbar müsste eigentlich immer gleich implementiert sein.
# Es ist also egal ob ich von der \index.html die .\about,html aufrufe od ero bich ausgehend von Docus\Programmoerien\Python.html die Seite .\aboutt aufrufe.
# und von dort aus die Navigationsleiste immer auf die gleiche Art zu testetn
# Die navigation wurde inital einmalig erstellt und wurde in alle nachgelagerten Webpages idetnisch implementiert.
from selenium import webdriver
import sys
import time
import re
import os
import ast

url = sys.argv[1]
ListOfClicksString = sys.argv[2]
ListOfClicks =  ast.literal_eval(ListOfClicksString)

skriptname = os.path.basename(__file__)
error = ""


driver = webdriver.Chrome()
driver.get(url)

for basicElement in ListOfClicks:
    if("[" in str(basicElement)):
        pass
    else:
        #basicElement ="single"
        basicElement= "['" + basicElement + "']"
        basicElement = ast.literal_eval(basicElement)
        
    for singleClick in basicElement:
        try:
            navField = driver.find_element_by_name(singleClick)
            navField.click()
            time.sleep(2)
        except:
            error = "Fehler im Skript " + str(skriptname) + ". Der Klickweg:\n" + str(basicElement) + "\nkonnte nicht aufgerufen werden.\n\n\n"

if(error != ""):
    f = open("01_navBarTesting-Basic_ERROR.txt", "a")
    f.write(error)
    f.close()

driver.close()


'''ListOfClicks = ListOfClicks.replace("[", "")
ListOfClicks = ListOfClicks.replace("]", "")
ListOfClicks = ListOfClicks.replace(" ", "")
ListOfClicks = re.split(",", ListOfClicks)

skriptname = os.path.basename(__file__)
error = ""


driver = webdriver.Chrome()
driver.get(url)

for basicClick in ListOfClicks:
    try:
        navField = driver.find_element_by_name(basicClick)
        navField.click()
    except:
        error = "Fehler im Skript " + str(skriptname) + ". Der Baseclick:\n" + str(basicClick) + "\nkonnte nicht aufgerufen werden.\n\n\n"

if(error != ""):
    f = open("01_navBarTesting-Basic_ERROR.txt", "a")
    f.write(error)
    f.close()

driver.close()

'''

    

