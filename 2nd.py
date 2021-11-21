import random

# To initialize the game, my program will randomly generate a couple of numbers, which will be used for you to calculate.
First = random.randint(0,99) 
Second = random.randint(0,99)


# This records your score, it will define your skill at the end of the game. 
score = 0


# Now, the game begins, the program will generate the numbers for the 10 items, do your best and Goodluck! 
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

Ninth = random.randint(0,99) 
Tenth = random.randint(0,99)


print (Ninth, Tenth)
PanlimangQuestion = int(input("What is the sum of the given numbers?: "))
AnoSum5 = Ninth + Tenth
if AnoSum5 == PanlimangQuestion:
    print ("Correct")
    score = score + 1
elif AnoSum5 != PanlimangQuestion: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)


Eleventh = random.randint(0,99) 
Twelfth = random.randint(0,99)


print (Eleventh, Twelfth)
PanganimNaQuestion = int(input("What is the sum of the given numbers?: "))
AnoSum6 = Eleventh + Twelfth
if AnoSum6 == PanganimNaQuestion:
    print ("Correct")
    score = score + 1
elif AnoSum6 != PanganimNaQuestion: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    

Thirteenth = random.randint(0,99) 
Fourteenth = random.randint(0,99)


print (Thirteenth, Fourteenth)
PampitongTanong = int(input("What is the sum of the given numbers?: "))
AnoSum7 = Thirteenth + Fourteenth
if AnoSum7 == PampitongTanong:
    print ("Correct")
    score = score + 1
elif AnoSum7 != PampitongTanong: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    


Fifteenth = random.randint(0,99) 
Sixteenth = random.randint(0,99)


print (Fifteenth, Sixteenth)
PangwalongTanong = int(input("What is the sum of the given numbers?: "))
AnoSum8 = Fifteenth + Sixteenth
if AnoSum8 == PangwalongTanong:
    print ("Correct")
    score = score + 1
elif AnoSum8 != PangwalongTanong: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)    


Seventeenth = random.randint(0,99) 
Eighteenth = random.randint(0,99)


print (Seventeenth, Eighteenth)
PangsiyamNaTanong = int(input("What is the sum of the given numbers?: "))
AnoSum9 = Seventeenth + Eighteenth
if AnoSum9 == PangsiyamNaTanong:
    print ("Correct")
    score = score + 1
elif AnoSum9 != PangsiyamNaTanong: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)


Nineteenth = random.randint(0,99) 
Twentieth = random.randint(0,99)


print (Seventeenth, Eighteenth)
IkaSampungTanong = int(input("What is the sum of the given numbers?: "))
AnoSum10 = Seventeenth + Eighteenth
if AnoSum10 == IkaSampungTanong:
    print ("Correct")
    score = score + 1
elif AnoSum10 != IkaSampungTanong: 
    print ("Unfortunately, you are wrong")
    score = score + 0

print (score)


# After you have completed the game, the program will commend you for your efforts, if you failed "practice makes perfect".
if score == 10:
    print ("Excellent Job")
    print ({score}/10)
elif score == 9:
    print ("Very Good")  
    print ({score}/10)  
elif score == 8:
    print ("Good")
    print ({score}/10)
elif score == 7:
    print ("Well Done")     
    print ({score}/10)
elif score == 6:
    print ("Good Effort")   
    print ({score}/10)
elif score == 5:
    print ("Better luck next time")    
    print ({score}/10)
elif score == 4:
    print ("Need More Practice")    
    print ({score}/10)
elif score == 3:
    print ("Need More Practice")    
    print ({score}/10)
elif score == 2:
    print ("Need More Practice")    
    print ({score}/10)
elif score == 1:
    print ("Need More Practice")    
    print ({score}/10)
elif score == 0:
    print ("Consult with your teacher if you need help")    
    print ({score}/10)               
    