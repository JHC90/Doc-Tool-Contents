# Hello world

## Basic
hier gehts es lediglich um die Endung einer html Datei.
Sobald lokal eine HTML-Datei geöffnet wird öffnet sich der Browser. Konkret Müssen dafür nicht mal die HTML-Tags verwendet werden. 
Dies "unformatierten" Seiten können auch von einem Webserver bereitgestellt werden. 

Hier ein Beispiel einer simplen HTML Datei ohne Doctype und ohne Tag-Struktur:

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/01_html/01_helloworld" width="80%" height="500"></iframe> <br>




# Doctype
Der Doctype hat nicht direkt was mit dem dargestellten Content zu tun. Dennoch werden im Content wichtige Metadaten für die gegenwärtige HTML Datei enthalten. BSP Author, Sprache, Encoding, Link zu CSS & JS usw. Die untere Seite hat zwar die gleiche

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/01_html/01_a_helloworld" width="80%" height="500"></iframe> <br>






# HTML-Struktur

Die Grundstruktur lautet

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title></title>
        ...
        <style>In CSS</style>
    </head>
    <body>
        <header>
        </header>
        <content>
        </content>
        <footer>
        </footer>

    </body>
</html>
```

Mit dieser Struktur können später die Inhalte von CSS direkt angesprochen und vernünftig formatiert werden.