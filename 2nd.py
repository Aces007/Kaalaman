import random


Una = random.randint(0,99) 
Pangalawa = random.randint(0,99)

score = 0

print (Una, Pangalawa)
UnaTanong = int(input("What is the sum of the given numbers?: "))
AnoSum = Una + Pangalawa
if AnoSum == UnaTanong:
    print ("Correct")
    score = score + 1
elif AnoSum != UnaTanong: 
    print ("Unfortunately, you are wrong")
    score = score = 0
    
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
    
