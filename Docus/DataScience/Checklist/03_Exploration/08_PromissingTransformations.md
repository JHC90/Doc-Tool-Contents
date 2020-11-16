'''''
{
"title": "Explore the Data - Promissing Transformations",
"keywords": "Checkliste, ListData",
"categories": "",
"description": "Hier geht es darum zu ermitteln und niederzuschreiben welche Daten ebnötigt werden",
"level": "10",
"pageID": "07112020200718-PromissingTransformations"
}
'''''

# Beispiel
es werden gerne Relative Zahle eingeführt. z.B.:
```Python
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"]=housing["population"]/housing["households"]
```



