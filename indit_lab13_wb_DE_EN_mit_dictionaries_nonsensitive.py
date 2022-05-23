# Aufgabe: Erweitern und ändern Sie das Wörterbuch Beispiel unter Verwendung eines Dictionarys

woerterbuch = {"Apfel":"apple", "Birne":"pear", "Kirsche":"cherry", "Melone":"melon", "Marille":"apricot", "Pfirsich":"peach"}

index = 0   # Zählervariable


# 1. Ermittlung Länge Wörterbuch (= Anzahl Eintargspaare)
# Umwandlung dictionary zu 2 listen um case non sensitive abfragen zu können

max = len(woerterbuch)                       # Grenze für Schleife definieren
woerterbuch_de = list(woerterbuch.keys())    # Liste der deutschen Begriffe (=keys)
woerterbuch_en = list(woerterbuch.values())  # Liste der englischen Begriffe (=values)
# print (woerterbuch_de[index])              # test


# 2. Eingabe

key = input("Deutscher Begriff: ")


# 3. while-Schleife mit if-Abfrage, case non sensitive, es werden nur die 2 Listen verwendet
# Funkt. auch mit slice?
    
while index < max:
    if woerterbuch_de[index].upper() == key.upper():    
        print("Englischer Begriff:" , woerterbuch_en[index])
        break
    index +=1
    
if index == max:
    print("Begriff nicht gefunden")
