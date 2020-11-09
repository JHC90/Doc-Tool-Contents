import re
import os
from glob import glob
import pandas as pd

def printDebugErrorPart(location, message):   
    '''
    Für den Debug-Mode gebe die exakte Stelle der Problematik zurück
    '''
    print("###")
    print(location)
    print(message)
    print("###")
    print("\n")

def retrungCategoriesList(x):
    '''
    Extrahiere die Kategorie Informaitonen vondem pfad und gebe eine Liste zurück
    '''
    x = x.replace("C:/DocTool/content/", "")
    x = re.split("/", x)[:-1]
    return(x)

def returnWebAdresse(x):
    '''
    Extrahiere die Pfade, sodass die Webadresse ableitbar ist
    '''
    x = x.replace("C:/DocTool/content/", "https://jhc90.github.io/")
    x = x.replace(".md", ".html")
    return(x)

def retrunSection(x):
    '''
    Extrahiere die Pfade, sodass die Webadresse ableitbar ist
    '''
    if(len(x) == 0):
        x = x
    else:
        x = x[-1]
    return(x)

def transformCSVsToList(x):
    '''
    Extrahiere die Pfade, sodass die Webadresse ableitbar ist
    '''
    x = re.split(",", x)
    return(x)

def returnSectionPathAbsolute(x):
    '''
    Extrahiere die absoluten Pfade für die Sections
    '''
    x = re.split("/", x)[:-1]
    y=""
    for element in x:
        y = y + element + "/"
    x = y
    return(x)

def returnSectionPathRelative(x):
    '''
    Extrahiere die absoluten Pfade für die Sections
    '''
    x = x.replace("C:/DocTool/content", "")
    if(x == ""):
        x = "/"
    return(x)


def recursiveFolderHandling(currentFolder, navbar, metaInfosPDDF):
    '''
    Erstellen der rekursiven Navigationserstellung
    '''
    print("WelcomeFunction")
    # Alle Files = html & md
    files = os.listdir(currentFolder)
    listOfAllMarkDownFilesInCurrentFolder = [i for i in files if i.endswith('.md')]
    listOfAllHTMLFilesInCurrentFolder = [i for i in files if i.endswith('.html')]
     
    listOfAllFilesInCurrentFolder = listOfAllMarkDownFilesInCurrentFolder + listOfAllHTMLFilesInCurrentFolder
    
    # Alle FilFolderes
    listOfDirs=glob(currentFolder+"*/")
    finalBaseFolderListSecond = []
    for i in range(0,len(listOfDirs),1):
        listOfDirs[i] = listOfDirs[i].replace("\\","/")
        if("imgs" in listOfDirs[i]):
            continue
        if("imgs" in listOfDirs[i]):
            continue
        elif("datasets" in listOfDirs[i]):
            continue
        elif("images" in listOfDirs[i]):
            continue
        elif("images" in listOfDirs[i]):
            continue
        elif("00_Doc-Tool" in listOfDirs[i]):
            continue
        else:
            name = listOfDirs[i].split("/")[-2]
            finalBaseFolderListSecond.append([listOfDirs[i], name])

    # auslesen der gegenwärtigen Seite und der zugehörigen MetaInfos
    
    

    # Füge gegenwärtigen ordnerSpezifschen Content zur nav hinzu hinzu
    navbar = navbar+'<ul class="dropdown-menu">'
    # hier die Files 
    for eachFile in listOfAllFilesInCurrentFolder:
        
        name = (eachFile.split(".")[0])
        filetype = (eachFile.split(".")[1])
        path = currentFolder +  eachFile
        path = path.replace("content/","")
        
        filtervalue = path[1:]
        
      
        
        filteredDF  = metaInfosPDDF.loc[metaInfosPDDF['fileNameRelative'] == filtervalue]
        print(filtervalue)
        level = int(filteredDF['level'])
        print(level)       
        print("")

        
        navbar = navbar+'<li name="' + str(name) +  '" tabindex="' + str(level) +  '"><a href="' + str(path) + '">' + str(name) + '</a></li>'

    # hier die ordner
    for eachfolder in finalBaseFolderListSecond:
        navbar = navbar + '<li class="dropdown-submenu" name=' + str(eachfolder[1]) + '><a class="test" tabindex="-1" href="#">' + str(eachfolder[1]) + '<span class="caret"></span></a>'
        navbar = recursiveFolderHandling(eachfolder[0], navbar, metaInfosPDDF)
        navbar = navbar + '</li">'
         
    navbar = navbar+'</ul>'
    return(navbar)