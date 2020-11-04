# call:
# Seite gibt es
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python .\00_basicWebsiteAvailiblity.py https://www.google.de
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python .\00_basicWebsiteAvailiblity.py file:///C:/DocTool/output/Docus/DataScience/Praxis/handson-ml/01_the_machine_learning_landscape.html
# Seite gibt es nicht
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python .\00_basicWebsiteAvailiblity.py http://fazrbnok.de/
# cd 'C:\DocTool\content\Projekte\00_Doc-Tool\TestWebsite\'; python .\00_basicWebsiteAvailiblity.py file:///C:/DocTool/output/Docus/DataScience/Praxis/handson-ml/01_the_machine_learning_landscape123.html
import sys
import os
import time
from selenium import webdriver

url = sys.argv[1]
skriptname = os.path.basename(__file__)
print()
#driver = webdriver.Chrome()
driver = webdriver.Firefox()

error = ""

try:
    driver.get(url)
except:
    error = "Fehler im Skript " + str(skriptname) + ".Die URL:\n" + str(url) + "\nkonnte nicht aufgerufen werden.\n\n\n"

if(error != ""):
    f = open("00_basicWebsiteAvailiblity_ERROR.txt", "a")
    f.write(error)
    f.close()

driver.close()