'''''
{
"title": " Cascading Style Sheet - Basics",
"keywords": "CSS, Basics",
"categories": "",
"description": "Hier ein Überblick über die CSS-Basics, ein Beispiel was damit erstellt werden kann",
"level": "00",
"pageID": "091120200813-Basics"
}
'''''



# Cascading Style Sheet

## Beispiel Implementierung
Nachdem nun die Inhalte von [HTML](./../HTML/01-HTML-Grundlagen.md) kommen kann mit CSS nun das Styling der Seite definiert werden. Ein möglicher Output sieht wiefolgt aus. 

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/cssprojekt" width="100%" height="300px"></iframe>

Der Iframe dient nur dazu zu erkennen welche Technologien man in dem CSS Sektion erlernt und was diese letztlich können.


## Sinnvolle Vorwissen
- [HTML-Grundlagen](./../HTML/01-HTML-Grundlagen.md)
- [HTML-Content](./../HTML/02-HTML-TextEingaben.md)
## Optionen CSS einzubinden:
|   | inline  | internal  |  external |
|---|---|---|---|
|Beschreibung|Der Style wird innerhalb des jeweiligen Tags angelegt| Der Style wird innerhalb des Style Tags innerhalb des Heads verwaltet| Die CSS-Config ist in einer seperaten Datei ausgelagert|
|Bsp-Seite|<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.3+inline+css"></iframe> <br>|<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.3+internal+css"></iframe> <br>|<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.3+external"></iframe> <br>
|ausgelagerte CSS|nein|nein|ja, neue Datei, im gegensatz zu internal braucht es keine \<style\>-Tags, und im html muss noch die CSS aufgerufen werden im header



Hier die drei CSS-Implementierungsoptionen. An live Projekten arbeitet man immer mit external CSS. In diesem Block hier arbeite ich überwiegend mit den Internal CSS, da die Snippets hier lediglich als vorlagen dienen. 



<div id="tabpanel">
  <ul role="tablist" id="tablist">
    <li id="link1" role="tab" aria-controls="panel-1" aria-selected="true">1 - Button</li>
    <li id="link2" role="tab" aria-controls="panel-2" aria-selected="false">2 - Button</li>
    <li id="link3" role="tab" aria-controls="panel-3" aria-selected="false">3 - Button</li>
  </ul>
 
  <div id="tabcontent">
    <div id="panel-1" role="tabpanel" aria-labelledby="link1" aria-hidden="false">
      <h3>Inhalt 1</h3>
      <p> Hier kommt was hin!</p>
    </div>
    <div id="panel-2" role="tabpanel" aria-labelledby="link2" aria-hidden="true">
    <h3>Inhalt 1</h3>
      <p> Hier kommt was hin!</p>
    </div>
    <div id="panel-3" role="tabpanel" aria-labelledby="link3" aria-hidden="true">
      <h3>Inhalt 1</h3>
      <p> Hier kommt was hin!</p>
    </div>
  </div>
</div>

#tablist {
  list-style: none;
  margin: 0;
  padding: 0;
}

