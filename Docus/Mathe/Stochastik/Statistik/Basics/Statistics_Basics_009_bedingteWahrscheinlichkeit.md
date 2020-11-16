# Bedingte Wahrscheinlichkeit

## Teaser
Davor [Bedingte Wahrscheinlichkeiten](./Statistics_Basics_009_bedingteWahrscheinlichkeit.md) durchmachen.


Die Wahrscheinlichkeiten von Ereignis A kann sich verändern, vorausgesetzt das Ereignis B ist bereits eingetreten. Hier spricht man von einer bedingten Wahrscheinlichkeit.
Die Formel hierzu lautet

				𝑃 (𝐴 | 𝐵)

## Erklärung

Zurück zu abhängigen Ereignissen ist die Wahrscheinlichkeit, zwei rote Kugeln zu ziehen:

		𝑃(𝑅_1∩𝑅_2)=𝑃(𝑅_1 )∙𝑃(𝑅_2 |𝑅_1 )

Die Bedingung in dieser Gleichung ist:

		𝑃(𝑅_2 |𝑅_1 )

Das Umstellen der Formel ergibt:
		
		 𝑃(𝐴│𝐵)=𝑃(𝐴∩𝐵)/(𝑃(𝐵))

Das heißt, die Wahrscheinlichkeit von A unter der Bedingung, dass B eingetreten ist,ist gleich der Wahrscheinlichkeit von A und Bdividiert durch die Wahrscheinlichkeit von B

## BSP
Ein Unternehmen stellt fest, dass von 100 Projekten 48 pünktlich fertiggestellt, 62 im Rahmen des Budgets abgeschlossen und 16 pünktlich und im Rahmen des Budgets abgeschlossen werden.
Wenn ein Projekt pünktlich fertiggestellt wird, wie hoch ist die Wahrscheinlichkeit, dass es unter dem Budget liegt?


A = 48 || Pünktlich
B = 62 | Budget
𝐴∩𝐵 = 16 | beides


𝑃(B│A)=𝑃(B∩A)/(𝑃(A)) = 16/48 = 0.33

