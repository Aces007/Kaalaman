import random


First = random.randint(0,99) 
Second = random.randint(0,99)

score = 0

print (First, Second)
UnaTanong = int(input("What is the sum of the given numbers?: "))
AnoSum = First + Second
if AnoSum == UnaTanong:
    print ("Correct")
    score = score + 1
elif AnoSum != UnaTanong: 
    print ("Unfortunately, you are wrong")
    score = score = 0
    
print (score)    

Third = random.randint(0,99) 
Fourth = random.randint(0,99)


print (Third, Fourth)
PangalawangQuestion = int(input("What is the sum of the given numbers?: "))
AnoSum2 = Third + Fourth
if AnoSum2 == PangalawangQuestion:
    print ("Correct")
    score = score + 1
elif AnoSum2 != PangalawangQuestion: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    

Fifth = random.randint(0,99) 
Sixth = random.randint(0,99)


print (Fifth, Sixth)
PangatlongQuestion = int(input("What is the sum of the given numbers?: "))
AnoSum3 = Fifth + Sixth
if AnoSum3 == PangatlongQuestion:
    print ("Correct")
    score = score + 1
elif AnoSum3 != PangatlongQuestion: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    


Seventh = random.randint(0,99) 
Eighth = random.randint(0,99)


print (Seventh, Eighth)
PangapatQuestion = int(input("What is the sum of the given numbers?: "))
AnoSum4 = Seventh + Eighth
if AnoSum4 == PangapatQuestion:
    print ("Correct")
    score = score + 1
elif AnoSum4 != PangapatQuestion: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    









    
