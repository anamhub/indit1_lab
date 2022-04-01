strIterationen = input("Anzahl der Iterationen: ")
intIterationen = int(strIterationen)
intZaehler = intIterationen-1

floatLeibniz = 0
floatPi = 0

while intZaehler >= 0:
    floatLeibniz += (-1)**intZaehler/(2*intZaehler+1)
    intZaehler -=1
    
floatPi = floatLeibniz*4    
print("Annäherung Pi bei", strIterationen, "Iterationen: ", floatPi)