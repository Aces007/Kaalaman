import random


Una = random.randint(0,99) 
Pangalawa = random.randint(0,99)

score = 0

def UnangTanong():
    print (Una, Pangalawa)
    UnaTanong = int(input("What is the sum of the given numbers?: "))
    AnoSum = Una + Pangalawa
    if AnoSum == UnaTanong:
        print ("Correct")
        print (score + 1)
    elif AnoSum != UnaTanong: 
        print ("Unfortunately, you are wrong")
        print (score)
    return UnaTanong, print (AnoSum)

Pangatlo = random.randint(0,99) 
Pangapat = random.randint(0,99)

def PangalawangTanong():
    print (Pangatlo, Pangapat)
    PangalawangQuestion = int(input("What is the sum of the given numbers?: "))
    AnoSum = Pangatlo + Pangapat
    if AnoSum == PangalawangQuestion:
        print ("Correct")
        print (score + 2)
    elif AnoSum != PangalawangQuestion: 
        print ("Unfortunately, you are wrong")
        print (score)
    return PangalawangQuestion, print (AnoSum)




PakitaFirst = UnangTanong()    
PakitaSecond = PangalawangTanong()