summand1 = float(input("Bitte summand1 eingeben:"))
summand2 = float(input("Bitte summand2 eingeben:"))

def fsumme(summand1, summand2):
    summe = summand1 + summand2
    return summe

def fdifferenz(summand1, summand2):
    differenz = summand1 - summand2
    return differenz

def fprodukt(summand1, summand2):
    produkt = summand1 * summand2
    return produkt

def fquotient(summand1, summand2):
    if summand2 == 0:
        print ("Mathematisch unmöglich")
        return
    quotient = summand1 / summand2
    return quotient

output1 = fsumme(summand1, summand2)
output2 = fdifferenz(summand1, summand2)
output3 = fprodukt(summand1, summand2)
output4 = fquotient(summand1, summand2)


print ("Summe:", output1)
print ("Differenz:", output2)
print ("Produkt:", output3)
print ("Quotient:", output4)



