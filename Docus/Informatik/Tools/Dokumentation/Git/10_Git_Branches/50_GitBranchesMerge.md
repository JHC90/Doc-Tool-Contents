'''''
{
"title": "Zusammenführen lokaler Branches",
"keywords": "git, branch, mergeBranches",
"categories": "",
"description": "Hier wird das Mergen von Git Branches lokal und remote innerhalb des CLI erklärt",
"level": "10"
}
'''''

<h1>git merge - zusammenführen zweier lokaler Branches</h1>

# git merge

hier wollen wir den Code von einem Branch retour in den ursprünglichen Folder mergen.

# bsp Ablauf 
1. Git checkout -b BRANCH_FROM_ORGINALBRANCH
2. Änderungen BRANCH_FROM_ORGINALBRANCH
3. Test der Änderungen in dem BRANCH_FROM_ORGINALBRANCH
4. git checkout ORGINALBRANCH
5. git merge BRANCH_FROM_ORGINALBRANCH

# bsp Ablauf Merge vom Remote Repo
Ein remote Branch muss nicht erst lokal ausgecheckt werden bevor er in den lokalen Branch gemergt werden kann

  > git merge /origin/featrue-101


jetzt wird direkt von remote in meinem aktuellen Branch gemerget
  