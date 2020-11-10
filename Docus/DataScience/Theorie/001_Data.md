
'''''
{
"title": "Data",
"keywords": "Data",
"categories": "Data",
"description": "Hier die Definition und die Aufteilung zu Data",
"level": "20",
"pageID": "07112020200718-Data"
}
'''''

<h1>Daten - Defintion entlang des DS-Prozesses</h1>

ML / DS / DL Modelle benötigen Daten. Dabei sind "Daten" nicht per se "Daten" in diesem Kontext. Diese Webpage gibt eine nkleinen aber feinen Überblick wie der Begriff Daten zu welchem Zeitpunkt in einem MDS-Project verstanden werden kann

---
---

## Gesamtes Dataset
Das sind alle Daten, auf welche wir zugreifen können. Normalerweise lädt man dieses Set von einer [REMOTE-Quelle](./../../Informatik/Programmieren/Python/Lösungen/00_DatenBeschaffung-Download.ipynb) herunter und lädt innerhalb eines DS-Projectes diese gesamten Daten zunächst in ein Data-Frame(entweder numpy oder Pandas) 

## Train-Data

Auf diesem Trainings-Set werden die Algorithmen trainiert.

---
---

## Test-Daten
Das ist das Set mit welchem wir die Performance des "von uns" trainierten Modelles testen. Somit wird das Modell ausschließlich auf den Trainingsdaten trainiert. 
Verwirrend wird es, da häufig in der Literatur Validieren und Testen as gleiche Begriffe verwendet werden.

 

---
---

## Validation-Set
Bei der Validierung wird sichergestellt, dass das "inzwischen" trainierte Modell gut generalisiert. 

Bei der Validation gibt es 2 Möglichkeiten der Implementierung
1. Das Validation-Set wird von dem **Gesamten Data-Set** gezogen. Dadurch entsteht "immer wieder" ein neues Trainings-Set
![Validation1](imgs/Validation1.gif)

---

2. Das Validation-Set wird ausschließlich von dem bereits gesplittetn **Training Data-Set** gezogen.
![Validation1](imgs/Validation2.gif)

Um diese Validation-Sets zu erstellen gibt es unterschiedliche Strategien. Diese werden [hier]() beschrieben

---
---






