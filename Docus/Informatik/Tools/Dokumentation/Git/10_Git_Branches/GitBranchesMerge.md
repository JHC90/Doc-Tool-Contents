# git merge

hier wollen wir den Code von einem Branch retour in den ursprünglichen Folder mergen.

# bsp Ablauf 
1. Git checkout -b BRANCH_FROM_ORGINALBRANCH
2. Änderungen BRANCH_FROM_ORGINALBRANCH
3. git chechout ORGINALBRANCH
4. git merge BRANCH_FROM_ORGINALBRANCH
  

  ![](imgs/2020-03-29-11-47-13.png)


  # bsp Ablauf Merge vom Remote Repo
Ein remote Branch muss nicht erst lokal ausgecheckt werden bevor er in den lokalen Branch gemergt werden kann

  > git merge /origin/featrue-101


jetzt wird direkt von remote in meinem aktuellen Branch gemerget
  