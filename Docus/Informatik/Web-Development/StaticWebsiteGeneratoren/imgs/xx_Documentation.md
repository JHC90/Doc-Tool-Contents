1) mkdir hugo_live
2) hugo new site hugo_live --force
3) cd hugo_live
4) tree
5) tree /f
6) hugo server -D => leere Seite aber keinen Fehler

# Überarbeitung config.toml
>baseURL =  "https://jhc90.github.io/"
>languageCode =  "de-de"
>title = "JHC-Jochen Hollich Consulting"
>theme = "basic"

# Erstelle Theme
1. >hugo new theme basic
2. Hinzufügen des Themes in die config.toml
 >theme = "basic"

 # Erstelle Website index
 >touch ./layouts/index.html 

 in dieser Datei muss nun auf den Inhalt von ./content/_index.html verwiesen werden
 ```html
 <!DOCTYPE html>
<html lang="de-de">
    <head>
        <meta charset="utf-8">
        <title>{{ .Site.Title }}</title>
    </head>
    <body>
        {{ .Content }}
    </body>
</html>
 ```
 3. touch ./content/_index.md => modifziere

 Testen ob server läuft => nach wie vor leer



# Erstelle etwas Inhalt mit Struktur
- hugo new Dokumentationen\_index.md
- hugo new Dokumentationen\Opeating-Systeme\_index.md

- hugo new Dokumentationen\Opeating-Systeme\Linux\_index.md
- hugo new Dokumentationen\Opeating-Systeme\Linux\bash.md

- hugo new Dokumentationen\Opeating-Systeme\Windows\_index.md
- hugo new Dokumentationen\Opeating-Systeme\Windows\cmd.md
- hugo new Dokumentationen\Opeating-Systeme\Windows\powershell.md

- hugo new Dokumentationen\Opeating-Systeme\MAC\_index.md
- 
- hugo new Dokumentationen\Programming\_index.md
- hugo new Dokumentationen\Programming\Python\_index.md

- hugo new Dokumentationen\Programming\Python\_index.md
- hugo new Dokumentationen\Programming\Python\Editoren_IDE_notebooks.md
- hugo new Dokumentationen\Programming\Python\Installation.md
- hugo new Dokumentationen\Programming\Python\Environment.md
- hugo new Dokumentationen\Programming\Python\kompilieren.md
- hugo new Dokumentationen\Programming\Python\Datentypen.md

- hugo new Projekte\Netzwerkanayse\_index.md
- hugo new Projekte\Netzwerkanayse\Datengeneration.md
- hugo new Projekte\Netzwerkanayse\Datenanalyse.md

**Bash**
```bash
hugo new Dokumentationen\_index.md && hugo new Dokumentationen\Opeating-Systeme\_index.md  && hugo new Dokumentationen\Opeating-Systeme\Linux\_index.md && hugo new Dokumentationen\Opeating-Systeme\Linux\bash.md  && hugo new Dokumentationen\Opeating-Systeme\Windows\_index.md && hugo new Dokumentationen\Opeating-Systeme\Windows\cmd.md && hugo new Dokumentationen\Opeating-Systeme\Windows owershell.md  && hugo new Dokumentationen\Opeating-Systeme\MAC\_index.md &&  && hugo new Dokumentationen rogramming\_index.md && hugo new Dokumentationen rogramming ython\_index.md  && hugo new Dokumentationen rogramming ython\_index.md && hugo new Dokumentationen rogramming ython\Editoren_IDE_notebooks.md && hugo new Dokumentationen rogramming ython\Installation.md && hugo new Dokumentationen rogramming ython\Environment.md && hugo new Dokumentationen rogramming ython\kompilieren.md && hugo new Dokumentationen rogramming ython\Datentypen.md  && hugo new Projekte\Netzwerkanayse\_index.md && hugo new Projekte\Netzwerkanayse\Datengeneration.md && hugo new Projekte\Netzwerkanayse\Datenanalyse.md 
```

**Powershell**
```powershell
rmdir -r .\content\;  mkdir content; hugo new Dokumentationen\_index.md; hugo new Dokumentationen\Opeating-Systeme\_index.md; hugo new Dokumentationen\Opeating-Systeme\Linux\_index.md; hugo new Dokumentationen\Opeating-Systeme\Linux\bash.md; hugo new Dokumentationen\Opeating-Systeme\Windows\_index.md; hugo new Dokumentationen\Opeating-Systeme\Windows\cmd.md; hugo new Dokumentationen\Opeating-Systeme\WindowsPowershell.md; hugo new Dokumentationen\Opeating-Systeme\MAC\_index.md; hugo new Dokumentationen programming\_index.md; hugo new Dokumentationen programming ython\_index.md; hugo new Dokumentationen rogramming ython\_index.md; hugo new Dokumentationen rogramming ython\Editoren_IDE_notebooks.md; hugo new Dokumentationen rogramming ython\Installation.md; hugo new Dokumentationen rogramming ython\Environment.md; hugo new Dokumentationen rogramming ython\kompilieren.md; hugo new Dokumentationen rogramming ython\Datentypen.md; hugo new Projekte\Netzwerkanayse\_index.md; hugo new Projekte\Netzwerkanayse\Datengeneration.md; hugo new Projekte\Netzwerkanayse\Datenanalyse.md 
```

![alt-Text](imgs/2020-10-20-08-26-23.png)




