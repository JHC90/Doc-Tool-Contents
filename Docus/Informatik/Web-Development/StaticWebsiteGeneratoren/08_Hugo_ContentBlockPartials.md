<h1>Content Blocks und Partials</h1>

Wenn hugo eien Webseite baut, werden der Inhatl von der Content section mit dem jeweiligen Layout file kombiniert. Diese Layout files wiederum greifen auf das Baseof zurück. Das baseof wiederum greift auf die Partials zurücks.

Die Partials sind die kleinsten elementaren Bausteiene bestehend aus HTML und go code.

## Sideinfo
das was für alle Seiten die Baseof ist, ist für die _index für die Hauptseite



# Content Block

Es gibt das **themes/basic/layouts/_default/baseof.html** File. Dies ist das Basefile, für jegliche weiter Seitensturkturen. In der einfachsten Form sieht dies so aus

```html
<!DOCTYPE html>
<html>
    {{- partial "head.html" . -}}
    <body>
        {{- partial "header.html" . -}}
        <div id="content">
        {{- block "main" . }}{{- end }}
        </div>
        {{- partial "footer.html" . -}}
    </body>
</html>
```

Im Body erkennt man wie unterschiedliche Inhalte von anderen layout vorlagen in das Base "hineingezogen werden". Durch diesen modularen aufbau können einzelne Eemente von unterschiedlichen Vorlagen verwendet weren

# Partials

Hier werden die einzelnen Bauelemente definiert

1. hier die Elemente
   1. Head
   ```html
   <!DOCTYPE html>
   <html>
      {{- partial "head.html" . -}}
      <body>
         {{- partial "header.html" . -}}
         <div id="content">
         {{- block "main" . }}{{- end }}
         </div>
         {{- partial "footer.html" . -}}
      </body>
   </html>
   ```
   2. Header
   ```html
   <header>
      <h1>{{ .Site.Title }}</h1>
   </header>
   <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
      <a href="/resume">Résumé</a>
      <a href="/contact">Contact</a>
   </nav>
   ```
   
   4. Footer
   ```html
   <footer>
      <small>Copyright {{now.Format "2006"}} Me.</small>
   </footer>
   ```

2. Sobald die drei partials definiert sind können die Layouts
- baseof.html
- single.html
- list.html

angpeasst werden. Dadurch wird bei der Konstruktion einer jeweiligen Seite auf dien entsprechenden Partials zugegriffen.
   1. Baseoff
   ```html
   <!DOCTYPE html>
   <html>
      {{- partial "head.html" . -}}
      <body>
         {{- partial "header.html" . -}}
         <div id="content">
         {{- block "main" . }}{{- end }}
         </div>
         {{- partial "footer.html" . -}}
      </body>
   </html>
   ```


   2. single.html
   ```html
   {{ define "main" }}
      <h2>{{ .Title }}</h2>
   {{ .Content }}
   {{ end }}
   ```

----------
Wrap up

Bisher haben wir unterschiedliche Seite erstellt
1) _index
2) _About

diese greifen beide auf utnerschiedliche Archtypes zu. Die Archtypes greifen wiederum auf die Partials zu. Wir nun auf unterschiedliche Layouts zu. Diese Layout besethen wiederum aus den Partials. Ein spezifischen Partial kann von utnerschieldichen Layouts verwendet werden- Somit können die Eigenschaften eines partials geändert werden. Dies hat dann Auswirkungen auf alle verlinkten Folder
   


