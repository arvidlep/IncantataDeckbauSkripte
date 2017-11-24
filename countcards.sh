#Greppt jede relevante Karte und addiert die Anzahlen
grep -E "9|[1-9][0-9]+" $1 | awk -F";" '{x+=$2}END{print "Anzahl Karten im Deck: " x}'
