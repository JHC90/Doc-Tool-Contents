'''''
{
"title": "Erstellen eines Remote Branches",
"keywords": "git, branch, remoteBranch",
"categories": "",
"description": "Hier wird das Anzeigen von Git Branches lokal und remote innerhalb des CLI erklärt",
"level": "10"
}
'''''

<h1>git checkout - Erstellen eines lokalen Branches</h1>


## Checkout Remote Branach

Remote Branch = Branch der am Remote Repo liegt, aber mir durch den Clone nicht notgedrungen mit heruntergeladen wird. Dieser Branch wurde von einem anderen Gerät aus erstellt, somit ist dieser Branch nicht bei mir lokal verfügbar. Wichtig ist dass derjenige der den Branch erstellt hatte. Diesen Branch auch auf Upstream gestellt hat. Dazu gibt es zwei möglichkeiten

1. der Branch wurde direkt im Webinterface von git erstellt. Dann wurde dieser Branch in das lokale repo des Kollegens geladen. Pushes von dem Kollegen werden in den Remote Branch gepusht
2. Der Kollege hat den Branch lokal erstellt. Soll dieser lokale Branch nun gepusht werden, so muss ein Upstream bestehen


Remote Branches im Remote-Repo kann man im Webinterface hier sehen:
![](imgs/2020-03-30-07-58-48.png).

Um lokal herauszufinden ob es remote Branches gibt muss man mit dem Befehl [git branch -a](./GitBranch.md) (!wichtig ist der Schalter -a) herausfinden ob remote Branches überhaupt existieren.  

zum [Checkout](./GitCheckout.md) einfach den klassisichen Checkout befehl mit dem Name (nicht dem ganzen Verzeichnis) von dem File

in diesem Beispiel gehtes um den Branch mit dem Verzeichnis "remotes/origin/feature101"(der noch nicht lokal exisitier) dieser wird nun mit dem Befehl 
> git checkout feature-101
> Ausgechcket und sist ab da lokal vorhanden

![](imgs/2020-03-30-07-55-32.png)