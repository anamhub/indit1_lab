# Labor 3 
# Ändern Sie das Wörterbuchbsp. aus Labor 2  wie folgt:
#
# 1) Verwendung eines oder mehrerer Assoziativ-Arrays (Dictionary)
# 2) Funktion, um übersetzte Begriffe auszulesen
# 3) Funktion, um dem Wörterbuch neue Begriffe hinzuzufügen

woerterbuch_DE_EN = {"Apfel":"apple", "Birne":"pear", "Kirsche":"cherry", "Melone":"melon", "Marille":"apricot", "Pfirsich":"peach"}
woerterbuch_EN_DE = {"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}

woerterbuch = {} # übernimmt das gewählte wörterbuch 

option_wb = input("Wählen Sie die gewünschte Funktion 1 = DE/EN oder 2 = EN/DE: ")
if option_wb == "1":
    woerterbuch = woerterbuch_DE_EN
elif option_wb == "2":
    woerterbuch = woerterbuch_EN_DE
else:
    woerterbuch = woerterbuch_DE_EN
    print ("Keine gültige Eingabe, Grundeinstellung Wörterbuch DE-EN ")
       
# Funktion für Menüauswahl:
def menu():
    print("Eingabe von [A]: Abfrage")
    print("Eingabe von [H]: Eintrag hinzufügen")
    auswahl = input("Auswahl: ")
    return auswahl

# Funktion für Abfrage:
def abfrage():
    eingegebene_abfrage = input("Ihre Abfrage: ")
    if eingegebene_abfrage in woerterbuch:
        value = woerterbuch[eingegebene_abfrage]
    else:
        value = "-"  # sonst können wir nichts zurückgeben
        print ("unbekannter Begriff")
    return value

# Funktion für Hinzufügen:
def hinzufuegen(begriff, ubersetzung):
    woerterbuch[begriff] = ubersetzung


# aufbau in einem loop
while True:

    ausgewaehlt = menu()
    #print(ausgewaehlt)  test ob menü richtige ausgabe gibt

    if ausgewaehlt == "A":
        ergebnis = abfrage()
        print("Übersetzung: ", ergebnis)

    if ausgewaehlt == "H":
        begriff = input("Begriff: ")
        ubersetzung = input("Übersetzung: ")
        hinzufuegen(begriff, ubersetzung)

    if ausgewaehlt == "Q":
        # aus dem Loop aussteigen; sonst mit Ctrl + D
        print("Auf Wiedersehen / Goodbye !")
        break


