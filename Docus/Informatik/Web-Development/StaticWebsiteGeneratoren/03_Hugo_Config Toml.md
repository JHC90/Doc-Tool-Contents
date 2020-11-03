<h1>Config-Datei</h1>

In dieser Datei werden die Grundlegenden Webseiten Informationen gepflegt.

Diese Datei kann in unterschiedlichen Dateiformaten erstellt sein. BSPW:
- toml
- yaml
- json

Für dieses Tutorial werde ich ausschließlich mit der TOML-Datei arbeiten.


## basic-Struktur der TOML-Datei 
```toml
baseURL =  "http://example.org/"
languageCode =  "en-us"
title =  "My New Hugo Site"
```

die BASE-URL ist die Domäne, auf welche die Webseite lauscht

Meine Basis-Struktur 
```toml
baseURL =  "https://jhc90.github.io/"
languageCode =  "de-de"
title =  "JHC-Portfolio"
```

Dieses Datei kann jedoch erheblich erweitert werden.


-----

Vergleiche die Basis-Struktur einer HTML, somit wird klar dass die Config-Toml die Basisdaten für den Head der HTML datei liefert

```toml
:<!DOCTYPE html>
<html lang= "en-US">  
    <head>    
        <meta charset= "utf-8">    
        <title>Title</title>  
    </head>  
    <body>
        <!-- some content goes here -->  
    </body>
</html>
```