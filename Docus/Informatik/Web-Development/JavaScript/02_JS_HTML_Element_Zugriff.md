<h1>Auf Elemente Zugreifen - </h1>

# Beschreibung

werden den Tags im Body IDs zugewiesen, so kann mit JS auf die Elemente zugegriffen werden.

- getElementById

ist hierbei ein zentraler JS-Befehl

Dadurch können sowohl der [HTML-Inhalt](./../HTML/01-HTML-Grundlagen.md) als auch das [Css-Styling](./../CSS/01_CSS_Basics.md) zugegirffen und geänder werden.

Diese Trigger können unterschiedlicher Natur sein
- Onclick
- Scroll

## Implementierung

Hier eine einfach Implementierung von Änderungn von Inhalt mittels JS. Hierbei wird noch kein Button(=Userinteraktion) verwendet

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/03_JS/3.3+auf+elemente+zugreifen"></iframe> <br>


<hr><hr><hr>

Die Folgende Implementierung des Buttons ändert sowohl den Inhalt als auch das Styling des P-Tags. Dabei gibt es bei den Tags Button einen "Trigger 'onclick'"

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/03_JS/3.4+auf+klicks+reagieren"></iframe> <br>

<hr><hr><hr>


Hier wird eine ähnliche Datei mit einem Button verwendet. Konkret wird hier jedoch die ID des p-Tags ausgelesen und mittels alert ausgegeben

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/03_JS/3.4+auf+klicks+reagieren2"></iframe> <br>


<hr><hr><hr>


Hier kommen weitere Funktionalitäten hinzu
1. Wird eine String-Concatination hinzugefügt. In Java-Script verwendet man hierbei die append Function
2. es kann auch HTML code hinzugefügt werden, Somit können die HTML-Tags allesamt verwendet werden. Somit kann der Inhalt und die HTML Darstellung mittels JS geändert werden.

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/03_JS/3.5+webseiteninhalte+anpassen.html"></iframe> <br>
