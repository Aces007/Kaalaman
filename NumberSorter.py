# 1st Step: This is the user input stage of the program, you will enter your numbers and the program will do all the sorting.
def PakilagayPoNgInyongNumbers():
    NumeroUno = int(input("Enter the first number you wish to sort: "))
    NumeroDos = int(input("Enter the second number you wish to sort: "))
    NumeroTres = int(input("Enter the third number you wish to sort: "))
    NumeroKwatro = int(input("Enter the fourth number you wish to sort: "))
    return NumeroUno, NumeroDos, NumeroTres, NumeroKwatro

# 2nd Step: This line here calls the returned values of the user input above, this is necessary in transferring your input values to the conditionals.
First, Second, Third, Fourth = PakilagayPoNgInyongNumbers() 
print (f"This is what we receieved from you, {First}, {Second}, {Third}, {Fourth}")

# 3rd Step: These conditionals are responsible for sorting the numbers from highest to lowest. They will be the one to do the job.
def LastPlace():
    if Fourth <= Third and Fourth <= Second and Fourth <= First:
        LastPlaceGoesTo = Fourth
    elif Third <= Fourth and Third <= Second and Third <= First:
        LastPlaceGoesTo = Third
    elif Second <= Fourth and Second <= Third and Second <= First:
        LastPlaceGoesTo = Second
    elif First <= Third and First <= Second and First <= Fourth:
        LastPlaceGoesTo = First

    return LastPlaceGoesTo

def FirstPlace():
    if Fourth >= Third and Fourth >= Second and Fourth >= First:
        FirstPlaceGoesTo = Fourth
    elif Third >= Fourth and Third >= Second and Third >= First:
        FirstPlaceGoesTo = Third
    elif Second >= Fourth and Second >= Third and Second >= First:
        FirstPlaceGoesTo = Second
    elif First >= Third and First >= Second and First >= Fourth:
        FirstPlaceGoesTo = First

    return FirstPlaceGoesTo

def ThirdPlace():
    if Inferior == (First):
        if Fourth < Third and Fourth < Second:
            ThirdPlaceGoesTo = Fourth
        elif Third < Fourth and Third < Second:
            ThirdPlaceGoesTo = Third
        else:
            ThirdPlaceGoesTo = Second
        return ThirdPlaceGoesTo

    if Inferior == (Second):
        if Fourth < Third and Fourth < First:
            ThirdPlaceGoesTo = Fourth
        elif Third < Fourth and Third < Second:
            ThirdPlaceGoesTo = Third
        else:
            ThirdPlaceGoesTo = First
        return ThirdPlaceGoesTo

    if Inferior == (Third):
        if Fourth < Second and Fourth < First:
            ThirdPlaceGoesTo = Fourth
        elif Second < Fourth and Second < First:
            ThirdPlaceGoesTo = Second
        else: 
            ThirdPlaceGoesTo = First
        return ThirdPlaceGoesTo

    if Inferior == (Fourth):
        if Third < Second and Third < First:
            ThirdPlaceGoesTo = Third
        elif Second < Third and Second < First:
            ThirdPlaceGoesTo = Second
        else: 
            ThirdPlaceGoesTo = First
        return ThirdPlaceGoesTo

def SecondPlace():
    if Superior == (First):
        if Fourth > Third and Fourth > Second:
            SecondPlaceGoesTo = Fourth
        elif Third > Fourth and Third > Second:
            SecondPlaceGoesTo = Third
        else:
            SecondPlaceGoesTo = Second
        return SecondPlaceGoesTo

    if Superior == (Second):
        if Fourth > Third and Fourth > First:
            SecondPlaceGoesTo = Fourth
        elif Third > Fourth and Third > Second:
            SecondPlaceGoesTo = Third
        else:
            SecondPlaceGoesTo = First
        return SecondPlaceGoesTo

    if Superior == (Third):
        if Fourth > Second and Fourth > First:
            SecondPlaceGoesTo = Fourth
        elif Second > Fourth and Second > First:
            SecondPlaceGoesTo = Second
        else: 
            SecondPlaceGoesTo = First
        return SecondPlaceGoesTo

    if Superior == (Fourth):
        if Third > Second and Third > First:
            SecondPlaceGoesTo = Third
        elif Second > Third and Second > First:
            SecondPlaceGoesTo = Second
        else: 
            SecondPlaceGoesTo = First
        return SecondPlaceGoesTo

# I labeled the numbers like this to be understandable lol.
Inferior = LastPlace()    
Superior = FirstPlace()
HenchMan = ThirdPlace()
SideKick = SecondPlace()


# Lastly: This print function will present you the summary of the arrangement.
print (f"So, based on the numbers you entered on the user inputs above; the simplified order from highest to the lowest, the arrangement of the digits are {Superior}, {SideKick}, {HenchMan}, {Inferior}")