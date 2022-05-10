# Programm, das auf 2 mgl. versionen, die in der Liste aufgeführten Personen begrüßt
# zB "Hallo, Peter!"
#
# Version 1: for-Schleife im Hauptprogramm, Ausgabe der Begrüßung in einem Unterprogramm
#
# Version 2: for-Schleife und Ausgabe der Begrüßung in einem Unterprogramm

liste_namen = ["Peter", "Dora", "Kevin", "Sarah"]


#Version 1
def begruessung(name):
    print("Hallo ", name)
    print("Schön dich zu sehen!")
    return
    
 

# Version 2
def begruessung2(namensliste): # definition = namensliste; def des param mit def d funkt fesgelegt
    for ein_name in namensliste:
        print("Hallo ", ein_name)
        print("Schön dich zu sehen!")
    return

# Ausgabe
print ("Version 1")
for name in liste_namen:
    begruessung(name)
    
print ("Version 2")
begruessung2(liste_namen)


    
    
    
  
    

