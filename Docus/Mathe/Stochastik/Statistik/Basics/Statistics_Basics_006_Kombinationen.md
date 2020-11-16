# Kombinationen

Ungeordnete Anordnungen von Objekten werden als Kombinationen bezeichnet.
Eine Gruppe von Personen, die ein Team bilden, bleiben die gleiche Gruppe, unabhängig der Reihenfolge.

Im gegensaetz zu Permutationen ist die Reohenfolge bei der Kombinatorik egal:

ABC == BCA => Kombinatorik
ABC != BCA => Permutation

## Formeln
### Kombination OHNE Wdh(bsp Leute aus eienm team || Pizza belegen, jede Zutat nur 1x)
$$_{n}C_{r} =   \frac{n!}{r!(n-r)!}$$
### Kombination MIT Wdh(b Pizza belegen, jede Zutat kann mehrfach)
$$_{n+r-1}C_{r} =   \frac{(n+r-1)!}{r!(n-r)!}$$

## Bsp:
Wie viele 3-Buchstaben-Kombinationen können aus den Buchstaben ABCDE gebildet werden?
### Kombinationen
n = 5 = Anzahl aller Ereginisse
r = 3 = Anzahl dieausgewählt wurde
$$_{n}C_{r} =   \frac{n!}{r!(n-r)!}$$
=> 
$$_{5}C_{3} =   \frac{5!}{3!(5-3)!} =  \frac{5!}{3!(2)! }= 10$$
### Permutaion im Verleich
$$_{5}P_{3} =   \frac{5!}{5-3)!} = 60$$

