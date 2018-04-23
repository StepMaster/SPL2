# zahlenraten.py
max = 200 #input ("Bitte geben Sie die maximale Zahl ein: ")
Mysterie = input ("Bitte gib deine Zahl ein: ")
Mysterie=int(Mysterie)
gewonnen = False
counter =0

zahl = max/2
zahl= int(zahl)

while(gewonnen == False):
    counter += 1

    if(zahl == Mysterie):
        gewonnen == True
        print("Er hat ", counter, " Versuche gebraucht")
        break

    elif(zahl < Mysterie):
        print("Zahl ist kleiner!")
        zahl=int(zahl/4*2)
     
        

    elif(zahl > Mysterie):

        print("Zahl ist groesser!")
        zahl = int((zahl/4*2)+zahl)

