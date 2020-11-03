<h1>Pagination</h1>

Wird ein größerer Inhalt, zum Beispiel ein langer Artikel auf einer Nachrichtenseite, auf mehrere Seiten aufgeteilt, spricht man von Pagination. In deutscher Sprache bedeutet Pagination so viel wie Seitennummerierung.

Implementierung:
1. es muss mehrere Blog-Einträge geben
2. blog/portfolio/themes/basic/layouts/posts/list_with_pagination.html

```
{{ define "main" }}
<h2>{{ .Title }}</h2>
» {{ range (.Paginator 1).Pages }}
{{ partial "post_summary.html" . }}
{{ end }}
» {{ template "_internal/pagination.html" . 
```

Hat noch nicht so gut geklappt. Konkret versucht man die Treffer in unterschiedliche Seitenzahlen zu unterteilen


# Comments

Hugo = static sites => Kommentarfunktion ausgelagert

Ich nutze das tool Disqus

# Gegenwärtig muss das bezahlt werden => mach ich nicht