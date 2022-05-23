# Aufgabe: Erweitern und ändern Sie das Wörterbuch Beispiel unter Verwendung eines Dictionarys

woerterbuch = {"Apfel":"apple", "Birne":"pear", "Kirsche":"cherry", "Melone":"melon", "Marille":"apricot", "Pfirsich":"peach"}

# 1. Eingabe

key = input("Deutscher Begriff:")

# 2. Abfrage 

if key in woerterbuch:
    value = woerterbuch[key]
    print(key, ":" , value)
    
else:
    print("Begriff nicht gefunden")
    
# funktioniert nur case sensitive
