import csv
import sys
import itertools

f = open(sys.argv[1], "r")
cards = []
reader = csv.reader(f, delimiter=";")

#CSV einlesen
for row in reader:
    cards.append([row[0], row[1]]);

#Jede Karte so oft wie sie gedruckt werden soll duplizieren
printNums = []
for card in cards:
    for _ in itertools.repeat(None, int(card[1])):
        printNums.append(int(card[0]));

#In 9er Gruppen aufteilen
printNumChunks = [printNums[i:i + 9]for i in range(0, len(printNums), 9)] 

#Links ausspucken
for chunk in printNumChunks:
    tmpStr = "http://127.0.0.1:43110/13VDeMgRgGf73mHsMrrorXkq4fhUKfBvPz/druck.html?ids=" + str(chunk[0])
    for i in range(1, len(chunk), 1):
        tmpStr += "," + str(chunk[i])
    print(tmpStr)

#print(printNumChunks)

f.close()
