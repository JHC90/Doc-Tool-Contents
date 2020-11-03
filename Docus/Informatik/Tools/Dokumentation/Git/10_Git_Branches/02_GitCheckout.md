<h1>git checkout - Erstellen eines lokalen Branches</h1>


Sofern man ein Repo öffnet, gibt es nicht den Zustand dass "kein Branch" gegenwärtig aktiv ist. Um einen neuen Branch zu kreieren oder um in einen Branch zu wechseln muss der gegenwärtig aktive Branch (der verlassen werden soll) commitet sein. (Ausnahme = git Stash)



mit dem Befehl:

> git checkout -b "Branchname"
> git checkout -b featureABC-Jira12-Userlogin

kann lokal ein Branch erstellt werden. mit dem Befehl:

>git branch
>git branch -a

wird verifiziert dass dieser Branch lokal erstellt wurde und aktiv ist. 








hier wollen wir von einem Branch in den anderen wechseln
Ähnlich wie [GitCreateBranches](./GitBranchCreate.md), beim Erstellen eines neuen Branches ist jedoch der Schalter -b wichtig. 

## Bsp am hotfix
> git checkout -b "hotfixNameNachNamingConvention"
 => erstellt neuen Branch


 > git checkout  "hotfixNameNachNamingConvention"
 => wechselt in den Branch

wenn der Branchname bereits existiert, wechselt man einfach in den jeweiligen Branch. Existiert der Name nicht, wird dieser erstellt. Wichtig beim erstellen wir der Branch da bagewzeigt, in welchem branch auch ever man sich in dem moment befindet

![](imgs/2020-03-29-11-22-46.png)

## Checkout Remote Branach

Remote Branch = Branch der am Remote Repo liegt, aber mir durch den Clone nicht notgedrungen mit heruntergeladen wird. 
Remote Branches kann man im Webinterface hier sehen:
![](imgs/2020-03-30-07-58-48.png).

Um lokal herauszufinden ob es remote Branches gibt muss man mit dem Befehl [git branch -a](./GitBranch.md) (!wichtig ist der Schalter -a) herausfinden ob remote Branches überhaupt existieren.  

zum [Checkout](./GitCheckout.md) einfach den klassisichen Checkout befehl mit dem Name (nicht dem ganzen Verzeichnis) von dem File

in diesem Beispiel gehtes um den Branch mit dem Verzeichnis "remotes/origin/feature101"(der noch nicht lokal exisitier) dieser wird nun mit dem Befehl 
> git checkout feature-101
> Ausgechcket und sist ab da lokal vorhanden

![](imgs/2020-03-30-07-55-32.png)