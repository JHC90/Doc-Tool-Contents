<h1>Static</h1>

Der folder Static beinhatet BIlder, skripte, Styles(css). Hier kann man sich somit mit den Waffen von css austoben. Somit bieten die Vortiele von DIV-Boxen alle Erweiterungen.

Das Stylesheet wird einmalig angelegt unter:

>portfolio\themes\basic\static\css

und wird dann im **head-Partial** hinterlegt. Somit ist das css in allen verwendeten 

```html
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ .Site.Title }}</title>
    <link rel= "stylesheet" href= "{{ "css/style.css"| relURL  }}">
</head>
```

Über diese Impelemntierung können nun auch die Elemente von Bootstrap in das Projekt mit einfließen