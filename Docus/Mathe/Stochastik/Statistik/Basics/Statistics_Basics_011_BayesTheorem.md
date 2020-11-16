# Bayes Theorem
<hr>
## Erklärung & Herleitung
Bayes Theorem = Erweiterung zu bedingte Wahrscheinlihckeit

Wir haben uns die bedingte Wahrscheinlichkeit bereits angesehen:
$P(A | B)=\frac{P(A \cap B)}{P(B)}$ mit $ P(B)>0$
$P(A \cap B)=P(A) \cdot P(B | A)$ mit $ P(A)>0$


Wir können nun die beiden Formeln zur bedingten Wahrscheinlichkeit in Beziehung setzen, und erhalten das Bayes Theorem:

$P(A | B)=\frac{P(B | A) \cdot P(A)}{P(B)} \operatorname{mit}  P(A), P(B)>0$


Das Bayes-Theorem wird verwendet, um die Wahrscheinlichkeit eines Parameters bei einem bestimmten Ereignis zu bestimmen.
Die allgemeine Formel lautet:
$$P(A | B)=\frac{P(B | A) \cdot P(A)}{P(B)}$$

<hr>

 ## BSP-Verwendung
 Ein Unternehmen erfährt, dass 1 von 500 oder 0,2% ihrer Produkte defekt ist. Das Unternehmen kauft ein Diagnose-Tool, das ein <mark>fehlerhaftes Teil zu 99% korrekt identifiziert (= 𝑃 (𝐵 | 𝐴) )  </mark>. Wenn ein Teil als defekt diagnostiziert wird, wie hoch ist die Wahrscheinlichkeit, dass es wirklich defekt ist?

<b>Schritt1:</b>
Definitionen:
𝑃 (𝐴) 	= Wahrscheinlichkeit, defekt zu sein
𝑃 ($\bar{𝐴}$) = Wahrscheinlichkeit NICHT defekt(=Funktionstüchtig) zu sein
𝑃 (𝐵) 	= Wahrscheinlichkeit, positiv zu testen(sowohl False & True Positive)
~Bedingte wahrscheinlichkeit
𝑃 (𝐴 | 𝐵) 	= Wahrscheinlichkeit, tatsächlich defekt zu sein, wenn positiv getestet wird 
𝑃 (𝐵 | 𝐴) 	= Wahrscheinlichkeit positiv zu testen, wenn Teil tatsächlich defekt

𝑃 (𝐵 | $\bar{𝐴}$𝐴) 	= Wahrscheinlichkeit positiv zu testen, wenn Teil NICHT defekt ist

<b>Schritt2:</b>
Klarstellen was gesucht ist: 

𝑃 (𝐴 | 𝐵) 	= Wert der gesucht wird
𝑃 (𝐵 | 𝐴) 	= 0,99 <= aus Angabe
𝑃 (𝐴) 	= 0,002 <= aus Angabe
𝑃 (𝐵) 	= Zwischenergbnis das für das eigentliche Ziel berechtnet werden muss

=> eigene weitere Herleitungen
𝑃 ($\bar{𝐴}$) 	= 1 - 𝑃 (𝐴) = 0.998
𝑃 (𝐵 | $\bar{𝐴}$) = 1 - 𝑃 (𝐵 | 𝐴) = 0.01 <= p positiv zu testen, wenn nicht defekt


<b>Schritt3:</b>
Klarstellen Begriffe: 
Echt Positiv 	= Produkt ist defekt und wird als defekt eingestuft
Falsch Positiv 	= Produkt ist nicht defekt, wird aber trotzdem als fehlerhaft eingestuft

<b>Schritt4:</b>
Berechen P(B) positv zu testen(sowohl true&False positive)<br>
𝑃 (𝐵) = Wahrscheinlichkeit, positiv zu testen<br>
		= P (echt positive) + P (falsch positive)<br>
		<mark>=𝑃(𝐵│𝐴)∙𝑃(𝐴)+𝑃(𝐵|−𝐴)∙𝑃(−𝐴)</mark> <= einsetzen in den Nenner der Formel vom Bayes Theorem<br>
		<br>
$P(A | B)=\frac{P(B | A) \cdot P(A)}{P(B)}$ => $\frac{P(B | A) \cdot P(A)}{P(B | A) \cdot P(A)+P(B |-A) \cdot P(-A)}$ => $\frac{0.99 \times 0.002}{0.99 \times 0.002+0.01 \times 0.998}$ = 0.165 ist die Wahrscheinlichkeit, dass ein Teil tatsächlich defekt ist, wenn der Test besagt dass Teil sei defekt

Zwischenfazit: Ein positiver Test hat eine Wahrscheinlichkeit von 16,5%, ein defektes Teil korrekt zu identifizieren. Anders ausgedrückt es werden viele Teile die nicht defekt sind als defekt gekennzeichnet.

Das ist nicht besonders hoch, daher werden alle Teile die nach dem ersten Test positiv gekennzeichnet sind, nochmals getestet. für die zweite Testmenge ergeben sich folgende Updates

in der 

𝑃 (𝐴) = Wahrscheinlichkeit, defekt zu sein = 0.165 (aus Ergbinis von Test1)
𝑃 ($\bar{𝐴}$) 	= 1 - 𝑃 (𝐴) = 0.835


$P(A | B)=\frac{0.99 \times 0.165}{0.99 \times 0.165+0.01 \times 0.835}$ = 0.951. Somit wäre nun die Wahrscheinlichkeit dass ein Teil dass





