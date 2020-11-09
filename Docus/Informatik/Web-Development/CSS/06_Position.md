'''''
{
"title": " CSS - Position",
"keywords": "CSS, Position"
"categories": "",
"description": "Hier eine Einführung zu Positioning in CSS",
"level": "60",
"pageID": "091120200814-Position"
}
'''''

# CSS-Positioning

## Vorwissen
- [Floating](./05_Floating.md)
 
## Postion
Im gegensatz zu [Floating](./05_Floating.md) gibt man beim Positioning etwas konkreter die Position des Elements an. 

Es kann auf zwei arten eine Positions übergeben werden
1. Absolute
hier wird das Element absolut positioniert & alle anderen Elemente ignorieren diese Position. Hierbei ist der absolute punkt immer die linke oberer Ecke

2. Relative
Alle Elemente die Relative verschoben. Relativ zu der Position, die das Element hätte, wenn keine relative Position hinterlegt = Ursprungsposition hätte haben sollen

3. fixed
Wenn ein Element beim Scrollen bestehen bleiben soll(BSP eine Nav-Bar), dann kann dies mit dem Position fixed erzielt werden. Damit kann bspw ein Konstantes Hintergrundbild unabhängig vom Scrollen implementier werden


## Troubleshooting
- z-Index = anordnugn "was liegt oben"
- opacity = durchsichtigkeit

## Implementierungen von Positioning
<hr>
<em>Ohne position</em>
<p>Hier ist noch kein Position implementiert. Der nachfolgende Iframe dient lediglich dem Vergleich zu anderen Position Optionen. </p>


<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.8+positioning"></iframe> <br>


<hr>
<em>Gegenüberstellung Absolute und Relativ</em>
<p>Hier ist noch kein Position implementiert. Der nachfolgende Iframe dient lediglich dem Vergleich zu anderen Position Optionen. </p>


'''tableConverterStart
| Relative  | Absolut  |
|---|---|
| <iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_css/2.8+positioning1relative"></iframe> <br> | <iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.8+positioning1Absolute"></iframe> <br> |
'''tableConverterEnd

<em>Float & Relative</em>
<p>hier wird die Position relative mit dem Float zusammengenommen </p>

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.8+positioning2"></iframe> <br>

<em>Fixed Position</em>
<p>Egal wie weit man scrollt die Rote box bleibt fixed an ihrer Stelle, das nutzt man gern bei Nav-Bars</p>

<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.8+positioning3" ></iframe> <br>


<iframe src="https://determined-varahamihira-d7b5b4.netlify.app/02_CSS/2.8+positioning4" ></iframe> <br>






