#!/bin/sh
#Entfernt allen whitespace und alles was in einer Zeile nach // steht
sed -e 's|//.*||g' $1 | tr -d "[:blank:]" | sed '/^$/d' > $2
