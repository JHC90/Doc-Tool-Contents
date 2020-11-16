# Hypothesentests

## Erklärung
* Ein Hypothesentest ist die Anwendung statistischer Methoden auf reale Fragen.
* Wir beginnen mit einer Annahme, der sogenannten Nullhypothese
* Wir führen ein Experiment durch, um diese Nullhypothese zu testen
* Basierend auf den Ergebnissen des Experiments können wir die Nullhypothese nun entweder annehmen oder ablehnen.
* Wenn die Nullhypothese zurückgewiesen wird, dann sagen wir, dass die Daten eine andere, sich gegenseitig ausschließende Alternativhypothese unterstützen.
* Wir "beweisen" nie eine Hypothese!

## Basics Null-Hypothes & Alternativ-Hypothese
Die Nullhypothese sollte eine Gleichung (=, ≤, ≥) enthalten:
	durchschnittliches Versandgewicht = 3.5kg
Die alternative Hypothese sollte ein Antonym (≠, <,>) enthalten:
	durchschnittliches Versandgewicht ≠ 3,5 kg




## Bsp. Hypothesen-Bildung
1. Wenn etwas, das als wahr angenommen wird, getestet wird, kann die Nullhypothese diese Annahme widerspiegeln:
Aussage: "Unser Produkt hat ein durchschnittliches Versandgewicht 			von 3,5 kg"
=>
Nullhypothese:			    Durchschnittsgewicht = 3,5kg
Alternativhypothese:		Durchschnittsgewicht ≠ 3,5 kg
2. Wenn wir eine Behauptung testen wollen, von der wir uns wünschen, dass sie wahr ist, wir dies aber nicht annehmen können, dann testen wir deren Gegenteil:
Behauptung: "Dieser Vorbereitungskurs verbessert die 						Testergebnisse"
=>
Nullhypothese:			alte Punkte ≥ neue Punkte
Alternativhypothese: 	alte Punkte < neue Punkte

Was also lässt uns die Nullhypothese zurückweisen oder nicht zurückweisen? => Hypothesentests

## Hypothesentests
Wir führen eine Untersuchung durch und speichern die Ergebnisse. 
Unter der Annahme, dass unsere Nullhypothese gültig ist und die Wahrscheinlichkeit, die getroffene Annahme zu beobachten sehr klein ist (innerhalb von 0,05), lehnen wir die Nullhypothese ab. Dazu brauch ich ein vorgegeben Signifikanzniveau(aus Angabe aus Business) α. Wenn α nicht angegeben ist dann ist dieses α = 0,05.

Kurz zusammengefasst: Ich berechene eine Teststatistik Z(= groß Z). Anschließend schlag ich je na Signifikanzniveau einen kritischen Wert z (= klein z)in der Z-Tabelle nach. Je nachdem welcher der Werte nun größer oder eben kleiner ist nehme ich die Nullhypothese nun an oder nicht. 

## Hypothesentests-Tails
Das Signifikanzniveau α ist das Gebiet innerhalb des Ablehnungsbereichs (Tail) unserer Nullhypothese.

* Left-Tail
  Wenn α = 0,05 und die Alternativhypothese <mark>kleiner</mark> als Null ist(vgl. dieses markdown "Bsp. Hypothesen-Bildung"), dann hat der linke Ablehnungsbereich (left-tail) unserer Wahrscheinlichkeitskurve eine Fläche von 0,05.
![](imgs/2020-03-26-08-52-25.png)

* Right-Tail
   Wenn α = 0,05 und die Alternativhypothese <mark>größer</mark> als Null ist(vgl. dieses markdown "Bsp. Hypothesen-Bildung"), dann hat der rechte Ablehnungsbereich (right-tail) unserer Wahrscheinlichkeitskurve eine Fläche von 0,05

![](imgs/2020-03-26-09-05-42.png)

* Two-Tail
  Wenn α = 0,05 und die Alternativhypothese <mark>ungleich</mark> Null ist, (vgl. dieses markdown "Bsp. Hypothesen-Bildung"),  dann haben beide Ablehnungsbereich (tails) unserer Wahrscheinlichkeitskurve eine Fläche von 0,05

![](imgs/2020-03-26-09-08-45.png)

<hr>
Diese Bereiche legen unsere kritischen Werte oder Z-Werte fest:

![](imgs/2020-03-26-09-11-39.png)

Wert1 = 0.0250
wert2 = 0.9750

Öffne  [Z-Tabelle](./Table-z-distribution.pdf) und suche nach dem entsprechenden Wert (vgl [Normalverteilung](./Statistics_Basics_015_Normalverteilung.md)) :
![](imgs/2020-03-26-09-31-13.png)

### !!! sonderfall Z-Wert ablesen
bei dem Heraussuchen gibt es einen Sonderfall In meiner [Beispielimplementierung](https://github.com/JHC90/Basic-DataScience-Skills/blob/master/Statistic-Basics/7_Hypothesentest_Mittelwert.ipynb) wird dieser behandelt. Konkret kann es vorkommen, dass ein 𝛼-Wert nicht in der Z-Table als tatsächliche Ausprägung auftritt(bsp 𝛼 = 0.01). In diesem Fall wählt man das "Gap, dass dem gewünschten 𝛼" am nächsten kommt, und berechnet einen Zwert der hierbei dazwischen liegt. Sprich bei 𝛼 = 0.01 (-2.32 + (-2.33))/2 = -2.325. Dieser -2.325 ist dann der Wert, welcher ür die weiteren Vergelichsschritte verwendet wird.
![](imgs/2020-03-26-11-43-20.png)


## Mittelwerttest vs. Häufigkeitstest
* Mittelwerttest (test of means)
  Wenn wir einen durchschnittlichen oder spezifischen Wert in einer Population suchen, haben wir es mit Mittelwerten zu tun
  Formel:
  $Z=\frac{\bar{x}-\mu}{\sigma / \sqrt{n}}$ // dazu brauchen wir $\sigma$(=std) der Population

* Häufigkeitstest (test of proportion)
  Wann immer wir etwas wie "35%" oder „hauptsächlich" sagen, handelt es sich um Häufigkeiten
  Formel:
  $Z=\frac{\hat{p}-p}{\sqrt{\frac{p \cdot q}{n}}}=\frac{\hat{p}-p}{\sqrt{\frac{p \cdot(1-p)}{n}}}$

## Annahme / Ablehnen einer Hypothese
Hierfür gibt es wiederum zwei Ansätze:
* traditionellen Test
nimm das Signifikanzniveau α
Verwende es, um den kritischen Wert zu bestimmen
Vergleichst du die Teststatistik mit dem kritischen Wert

* P-Wert-Test:
nimm die Teststatistik
verwende sie, um den P-Wert zu bestimmen
vergleiche den P-Wert mit dem Signifikanzniveau 𝛼

"If the P-value is low, the null must go!"
			lehne 𝑯_𝟎 ab

"If the P-value is high, the null must fly!"
			nehme 𝑯_𝟎 an

<hr>

## BSP-Implementierungen:
[IplementierungMittelwert](https://github.com/JHC90/Basic-DataScience-Skills/blob/master/Statistic-Basics/7_Hypothesentest_Mittelwert.ipynb)
[IplementierungHäufigkeiten](https://github.com/JHC90/Basic-DataScience-Skills/blob/master/Statistic-Basics/8_Hypothesentest_H%C3%A4ufigkeiten.ipynb)









