'''''
{
"title": "Statistic Basics - Definitionen",
"keywords": "Statistic-Basics",
"categories": "",
"description": "Hier die Erklärung meiner Webseite",
"level": "10",
"pageID": "16112020-KorrelationDefinition"
}
'''''

# Korrelation & Kovarianz
Bisher haben wir ein Feature jeweils isoliert betrachtet(Std & Varianz dienen nur für die Darstellung von jeweils einem Feature). Mit der Korrelation betrachten wir nun wie zwei Variablen zuammen sich verhalten. 

bei poisitiver Kovarianz = nehmen die Variabelen gemeinsam zu
bei negativer Kovarianz = nehmen die Variabelen vice versa zu und ab



[eigene Implementierung](https://github.com/JHC90/Basic-DataScience-Skills/blob/master/EDA_5_Correlations.ipynb)



## Begriffe
* Kovarianz<br> dimensionsloses Maß, das die Stärke der Zusammenhänge aufzeigt

* Korrelation<br>Im unterschied zur Kovarianz ist bei der Korrelation eine Standardisierung erfolgt => Vergleiche sind hierbei möglich

* Correlation Coefficinet <br> Maßzahl in welchem Ausmaß numerische Zahlen miteinander fungieren(von -1 bis +1)
* Correlation Matrix<br> Matrix die die numerischen Verbindungen der Correaltions-Coeffizienten darstellt || somit betrachtet eine Korrelationsmatrix die Kummulierte Darstelltung von zwei feature
* Scatterplot<br> heir werden zwei Variablen zusammen betrachtet. Sprich wenn x soundso hoch ist wie ist dann y
* Heatmap


## Eigenes Vorgehen
1. Erstelle Scatterplott
2. bei den Variablen von Interesse(stark +1 oder stark -1 oder 0) erstelle die Scatterplots


## Korrealtionskoeffizienten
* Populationskovarianz<br>
   $$cov(X,Y) =
  \frac{1}{N}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})$$
  
* Pearson-Korrelation
  * Formel<br>
  $$r =
  \frac{ \sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y}) }{%
        \sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}}$$
  * Auswahl<br>
* Spearman-Korrelation
  * Formel<br>
  * Auswahl<br>




## Correaltion Matrix
## Bsp-Korrelation
BildZumEinfügenInContainer

## Plots

## 2. Darstellung
hier eine Kombination aus der Korrelationmatrix & einer Heatmap für die IRIS-Daten
![](imgs/2020-03-26-08-12-51.png)

Positive Korrelation = +1
Keine Korrelation = 0
negative Korrelation = -1