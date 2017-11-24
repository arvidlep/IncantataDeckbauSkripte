# Incantata Deckbau Tools #

## Disclaimer ##

Ich bin zu diesem Zeitpunkt weder mit der bash noch mit python besonders gut vertraut, also ist der Code wahrscheinlich nicht sonderlich elegant (sei es mir verziehen).
Man betrachte diesen Code also bitte nicht als Demonstration meiner Programmierkünste, sondern als (hoffentlich) nützliches Geschenk.

## Die Skripte ##

### countcards.sh ###

Zählt alle für die Deckgröße relevanten Karten und gibt die Summe zurück.
Nicht gezählt werden Himmelskörper und Raumzeitgefüge.

*Anwendung*:
```
$ ./countcards.sh deck
```

### icdeckToCSV.sh ###

Macht eine icdeck Datei zu einer CSV Datei.
Dazu werden Kommentare und Whitespaces entfernt.

*Anwendung*:
```
$ ./icdeckToCSV.sh in.icdeck out.csv
```

### csvToNumbers.py ###

Nimmt eine CSV an und gibt zeilenweise fertige Drucklinks aus.

*Anwendung*:
```
$ python csvToNumbers.py deck.csv
```

## Wie mache ich ein neues Deck? ##

Man nehme einen Texteditor und schreibe einfach die Nummer der gewünschten Karte, dann ein Semikolon und dann die gewünschte Anzahl.
Das ganze macht man pro Karte in jeweils einer Zeile.

Whitespaces können nach Lust und Laune gesetzt werden, die werden sowieso entfernt.
Mit einem // kann ein Kommentar eingeleitet werden. Alles nach dem // wird ignoriert.

Beispielsweise will ich 1 Mantra der Reinheit (Nr. 1) und 6 Weiten (Nr. 9) im Deck haben, also schreibe ich:
```
//Ein sehr schönes Deck
1;1
9;6 //Länder kann man nie genug haben
```

## Was noch verbessert werden könnte ##

- Es wäre sicherlich nicht schlecht, ein viertes Skript zu schreiben, dass eine Datei als input bekommt und die anderen Skripte automatisch ausführt.
- Es ist immer platz für coole neue Features, z.B. einen Deckbauer oder eine automatische Validierung.

## Was bitte ist Incantata!? ##

Das wird hier demnächst stehen (sobald ich es selbst weiß).
