<h1>Front Matter</h1>

Das Front Matter ist der erste Teil eines Content Markdowns. Dieser Teil dient datzu die Metadaten des Markdowns zu strukturieren.

Dieses Front matter kann je nach gewünschten Seitentyp als Archtype angelegt werden. Wir nun eine Seite eines bestimmten Typs aufgerufen, so wird konkret diese Vorlage mit genutzt

```
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
---
```

Hier werden u.a. folgende Informationen gepflegt:
1. draft 
Diese Information gibt an ob die Seite mit gerendert wird oder nicht
2. Date
Gibt an, wann die Seite erstellt wurde
3. title
Gibt den title der Seite

