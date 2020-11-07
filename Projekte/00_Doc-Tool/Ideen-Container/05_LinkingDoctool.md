<h1>05_LinkingDoctool</h1>
ID = Filename = 05_LinkingDoctool

# Idee
Bisher laufen die Links innerhalb des Doctools via Makrdown und relativen Pfaden. Diese Links sind aber sobal sie angelegt sind "starrr". Wenn also sich das Ziel eines Links in dem Directory verschiebt führt der Link ins nirvana.  Die Idee ist jedem Markdown und Jupyter-Dokument im Front-Matter eine ID zuzuweisen. Linkaufrufeführen werden später mit IDs behandelt, somit kann sich das Ziel innerhalb der content section "frei" bewegen. Der Link wird somit immer zum gewünschten webpage hinter der ID führen 

# Technologien
- python

# Test
1) wenn bei der Ausführung des Skriptes
   1) Die Website gänzlich mit den den neusten Inhalten aus content erstellt wurde
   2) das Doc-Tool Repo gepusht wurde
   3) Das Output-Repo gepusht wurde


# Status der Idee

- [x]  Die Iddee exisitiert & Die Ideenentwicklung wurde gestartet
- [x]  Merge back to master
- [x]  Push Doc-Tool to remote master mit dem commit-Namen "01-DocTools-JPYNB-HTML-Converter"
- [x]  Lösche den lokalen Branch 
- [x]  Ideenimplementierung abgeschlossen

