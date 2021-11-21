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

Pangatlo = random.randint(0,99) 
Pangapat = random.randint(0,99)


print (Pangatlo, Pangapat)
PangalawangQuestion = int(input("What is the sum of the given numbers?: "))
AnoSum2 = Pangatlo + Pangapat
if AnoSum2 == PangalawangQuestion:
    print ("Correct")
    score = score + 1
elif AnoSum2 != PangalawangQuestion: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    


    
