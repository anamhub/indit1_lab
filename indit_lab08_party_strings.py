strWetter = input("Wie ist das Wetter (sonnig/regnerisch)? ")
# print("Das Wetter ist: ", strWetter)


if strWetter.lower() == "sonnig":
    print("Gartenparty!")
elif strWetter.lower() == "regnerisch":
    print("Kellerparty!")
else:
    print("Keine gültige Eingabe")