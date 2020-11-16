# Formelsammlung
### [Symbol-Definitionen](0_Symbol-Definitions.md)

<hr>
# <u>Lagemaße</u>
## Mittelwert / Mean
$\bar{x} = \frac{\sum_{i=1}^{n}x_{i}}{n}$ 
<hr>

# <u>Dispersion</u>
## Varianz

### Stichprobenvarianz
$s^2 = \frac{\sum (x-\bar{x})^2}{n-1}$ 

### Populationsvarianz
$\sigma^2 = \frac{\sum (X-\mu)^2}{N}$ 

## Standardabweichung
$\sigma = \sqrt{ \frac{\sum (X-\mu)^2}{N}}$ 

<hr>

# <u>Bivariate Maße</u>
## Populationskovarianz
$cov(X,Y) =   \frac{1}{N}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})$

## PearsonKorrelaitonskoeffizient
dazu brauch ich die Kovarianz der beiden Feature,und die Standardabweichungen der betracheten Featrue
$\rho _{x,y} =   \frac{cov(X,Y)}{\sigma_{x}\sigma_{y}}$

<hr>

# <u>Wahrscheinlichkeiten</u>
## Permutationen
### Anzahl der Permutationen einer Reihe
$n!$
### Permutation OHNE Wiederholung
$\ _{n}P_{r} =   \frac{n!}{(n-r)!}$
### Permutation MIT Wiederholung
$n^{r}$

## Kombinationen
 $n = Anzahl der Kombinationen $
 $r = gleichzeitig verwendete Objekte $

### Anzahl der Kombinationen OHNE WDH einer Reihe
$\ _{n}C_{r} =   \frac{n!}{r!(n-r)!}$
### Anzahl der Kombinationen MIT WDH einer Reihe
$_{n+r-1}C_{r} =   \frac{(n+r-1)!}{r!(n-1)!}$

<hr>

# <u>Verteilungen</u>
## <u>diskrete Verteilungen</u>
## Gleichverteilung
## Bernoulli-Verteilung
## Poisson-Verteilung
## <u>kontinuierliche Verteilungen</u>
### Normalverteilung
### Exponentialverteilung
### Betaverteilung






# Symbole
## Tabelle
n = Anzahl Instanzen = Zeilen
i = spezifische Auswahl für n || bspw die 2te beoabachtung = i = 2<
p = Anzahl Feature = Spalten
j = spezifische Auswahl für p || bspw das zweite Feature = i = 2
