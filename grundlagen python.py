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
wer = input("Und wer bist du?")

# und gibt den Text wieder aus
if (wer == "ich"):
    print ("Hallo DU!")
else:
    print("Hallo ",wer)

lieblingszahl = input("Was ist deine Lieblingszahl? ")
print ("Super, ich mag die Zahl ", lieblingszahl)
print ("Aber die cooler Zahl ", int(lieblingszahl)+1, " mag ich noch mehr!")

runden = input("Wie viele Runden sollen wir spielen? ")
runden = int(runden)

for runde in range(1, runden+1):
    zufallszahl=random.randint(1,6)

    if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger="ich"
    else:
        sieger = "Computer"
    print("Runde ",runde, "von",runden,": Sieger:",sieger)
print("Game Over.")