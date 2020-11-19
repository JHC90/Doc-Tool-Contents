'''''
{
"title": "DataPreparation - Feature Scaling",
"keywords": "Copy",
"categories": "",
"description": "Hier geht es darum zu ermitteln und niederzuschreiben welche Daten ebnötigt werden",
"level": "40",
"pageID": "07112020200718-FeatureScaling"
}
'''''

# Feature Scaling

![BannerChecklist](./../imgs/2020-11-19-08-20-02.png)

- normalisiere
- Standartisiere

Sind Daten über eine "große Spannweite" verteilt, so kann durch das Skalieren eine Vergleichbare Ebene geschaffen werden. Wichtig ist, das die skalierten Feature auch skaliert vorhergesagt werden. Das bedeutet, dass die vorhersagen auh "skaliert" sind. Folglich müssen vorhergesagte Werte zum Schluss wieder "reskaliert werden".

Die meisten Algorithmen funktionieren nicht "gut" wenn die unterschiedlichen Feature unterschieldich skalieren

# Typische Implementierungen
- min-max Scaling ~ normalization
- standardization (Werte zwischen 0&1)


