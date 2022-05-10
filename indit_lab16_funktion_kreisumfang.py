# Programm: Nach Eingabe des Radius in einer Funktion den Kreisumfang berechnen
# Verwendung pi aus math-Paket

#  die Eingabe soll in einer eigenen Funktion erfolgen, in der sichergestellt wird, dass es sich dabei:
#   a) allenfalls um eine Zahl
# und
#   b) eine positive Zahl handelt


import math

def eingabe():
    correct = False
    
    while correct == False:      #solange bis korrekte eingabe
            r_str = input("Eingabe Radius: ")
            # tests ob eingabe korrekt:
            try:
                r = float(r_str)
                if r > 0:
                    correct = True
                else:
                    print ("Zahl muss positiv sein")
            except ValueError:
                print ("Keine gültige Zahl")
                      
    return r


radius = eingabe()

kreisumfang = 2*math.pi*radius

print ("Kreisumfang: ", kreisumfang)