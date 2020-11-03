# Git Create Branch

bspw ein Featurebranch(~neues userlogin).


# Vorgehen
1. Create Feature Branch
   1. BranchName frei 
   Best Practise=> meist aber nach issue-Trackingsystem(Jira=> issue erhält ID => ID wird dann für den Branchname verwendet) und die Weiterführung wäre mit einem Projektname in der Namensbezeichnung:
2. Tatsächlicher git checkout

> git checkout -b "Branchname"
> git checkout -b featureABC-Jira12-Userlogin

zu 'git checkout -b "Branchname"' gibt es folenden redundanten Befehl
> git "Branchname" & git checkout "Branchname"

wird sind automatisch beim Checkout in den Branch gewechselt. das kann mit git Status angezeigt werden. 
3. Änderung in dem lokalen Repo, und im loaklen Repo in dem eigens erstellten Branch => git add & Git commit
4. git log
![](imgs/2020-03-29-10-53-06.png)
hier kann ich erkenne dass ich einen neuen Branch erstellt habe
ich kann auch sehen, dass die letzte Änderung auf dem FeatureBranch mit dem Namen SampleBranch erstellt habe. Diese Neue Datei ist lediglich in dem Featurebranch. 