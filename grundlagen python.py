# grundlagen python.py
import random
# Kommentare erfoölgen mit hashtag

# Ausgabe von Daten
print("Hallo World")

# Variablen definieren (kann ohne Typ erfolgen)
heimat = "Erde"

# Mehrere Variablen werden mit , getrennt
print (heimat, "an World: ", "Hallo")

# Eingabe / liest Text(!) von der Konsole ein
wer = input("Und wer bist du? ")

# und gibt den Text wieder aus
if (wer == "ich"):
    print ("Hallo DU!")
else:
    print("Hallo ",wer)

print("---------------------------------------------")
lieblingszahl = input("Was ist deine Lieblingszahl? ")
print ("Super, ich mag die Zahl ", lieblingszahl)
print ("Aber die cooler Zahl ", int(lieblingszahl)+1, " mag ich noch mehr!")
print("---------------------------------------------")
runden = input("Wie viele Runden sollen wir spielen? ")
runden = int(runden)
print("---------------------------------------------")

for runde in range(1, runden+1):
    zufallszahl=random.randint(1,6)
    zaehler1 = 0
    zaehler2 = 0

    if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger="ich"
        zaehler1=zaehler1+1
    else:
        sieger = "Computer"
        zaehler2=zaehler2+1
    print("Runde ",runde, "von",runden,": Sieger:",sieger)
    print("Gewuerfelte Zahl ist ",zufallszahl)

    print("---------------------------------------------")

if (zaehler1==zaehler2):
    print("Unentschieden")
elif(zaehler1<zaehler2):
    print("Computer hat gewonnen")

    print("Der Computer hat ",int(zaehler2)-int(zaehler1), "x oefter gewonnen")
elif(zaehler1>zaehler2):
    print("Du hast Gewonnen")
    print("Du hast ",int(zaehler1)-int(zaehler2), "x oefter gewonnen")



print("Game Over.")