# Lab 2/1:
# Programm, das in 10°-Schritten zw. 0° und 180° den jew. Cosinus-Wert berechnet und ausgibt

import math

intVar = 0     # Schrittzähler in Grad


print ("Cosinus-Wert Rechnung in 10°-Schritte:")

while intVar<=180:
    winkel_rad = intVar*math.pi/180
    cosinus = math.cos(winkel_rad)
    print ("cos(",intVar,"):", cosinus)
    intVar +=10




