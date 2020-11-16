# Permutation

Eine Permutation sind die Kombinationen einer Anordnung von Objekten in einer bestimmten Reihenfolge.

Im gegensaetz zu Permutationen ist die Reohenfolge bei der Kombinatorik egal:

ABC == BCA => Kombinatorik
ABC != BCA => Permutation


###########

Die möglichen Permutationen der Buchstaben a, b und c sind:

abc
acb
bac
bca
cab
cba




Für einfache Beispiele wie abc berechnen wir die Anzahl der möglichen Permutationen als 𝑛! („n faktoriell")
abc = 3 Items
𝑛! = 3! = 3 × 2 × 1 = 6 Permutationen


Man kann auch eine Teilmenge von Elementen in einer Permutation verwenden
Die Anzahl der Permutationen einer Menge 𝑛-Elemente mit 𝑟 gleichzeitig verwendeter Elemente, wird durch die folgende Formel ermittelt:
$$\ _{n}P_{r} =   \frac{n!}{(n-r)!}$$


# Bsp Permutation OHNE Wiederholung
Eine Website benötigt ein 4-stelliges Passwort
Zeichen können entweder Kleinbuchstaben (ohne Umlaute) oder die Ziffern 0-9 sein.
Kein Buchstabe oder kein Zeichen darf mehrfach verwendet werden
Wie viele verschiedene Passwörter kann es geben?

<b>Lösung OHNE Wiederholung</b>
Wir ermitteln also, dass 𝑛 oder die Anzahl der Objekte 26 Buchstaben + 10 Zahlen = 36 ist
𝑟, oder die Anzahl der gleichzeitig zu verwendenden Zeichen ist 4
Diese Zahlen setzen wir nun in die Formel ein:
$$\ _{36}P_{4} =   \frac{36!}{(36-4)!} = \frac{36!}{(32)!} = 1413720.0$$

# Permutation Mit Wiederholung
Die Anzahl der Permutationen einer Menge 𝑛-Items mit 𝑟 gleichzeitig verwendeter Items mit Wiederholung wird beschrieben in: $n^r$

## Bsp Permutation MIT Wiederholung
Wie viele 4-stellige Nummernschilder kann es mit den Ziffern 0 bis 9 geben, bei erlaubter Wiederholung der Ziffern

<b>Lösung MIT Wiederholung</b>
$$n^{r}=10^{4} = Permutationen = 10000$$

<b>Lösung OHNE Wiederholung</b>
$$\ _{10}P_{4} =   \frac{10!}{(10-4)!} = \frac{10!}{(6)!} = 5040.0$$



