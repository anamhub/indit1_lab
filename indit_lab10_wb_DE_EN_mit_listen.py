# Aufgabe: Wörterbuch DE --> EN

# Kurzes Programm, das nach Eingabe des dt. Begriffs die engl. Übersetzung ausgibt
# bzw. falls der Begriff nicht im Wörterbuch zu finden ist, eine entsprechende Meldung
# Kommentieren Sie Ihren Code


woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

index = 0   # Zählervariable

# 1. Eingabe

eingabe = input("Deutscher Begriff:")


# 2. Ermittlung Länge Wörterbuch (= Anzahl Einträge)

max = len(woerterbuch_deutsch)                    # Grenze für Schleife definieren


# 3. while-Schleife über alle Elemente
# 4. if-Abfrage zum Vergleich

while index < max:
    if woerterbuch_deutsch[index].upper() == eingabe.upper():    
        print(woerterbuch_english[index])
        break
    index +=1
    
if index == max:
    print("Begriff nicht gefunden")
    
   





