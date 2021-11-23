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
print ("We will just need a moment of your time...")

# 3rd Step: These conditionals are responsible for sorting the numbers from highest to lowest. They will be the one to do the job.
if Fourth <= Third:
    LastPlaceSi = Fourth
    ThirdPlacerSi = Third

elif Fourth > Third:
    ThirdPlacerSi = Fourth
    LastPlaceSi = Third

if Second <= ThirdPlacerSi:
    SecondPlacerSi = ThirdPlacerSi
    ThirdPlacerSi = LastPlaceSi
    LastPlaceSi = Second

elif Second >= ThirdPlacerSi:
    SecondPlacerSi = Second

if First >= SecondPlacerSi:
    WinnerSi = First

elif First <= SecondPlacerSi:
    WinnerSi = SecondPlacerSi
    SecondPlacerSi = ThirdPlacerSi
    ThirdPlacerSi = LastPlaceSi
    LastPlaceSi = First                       
    
# Lastly: This print function will present you the summary of the arrangement.
print (f"So, based on the numbers you entered on the user inputs above; the simplified order from highest to the lowest, the arrangement of the digits are {WinnerSi}, {SecondPlacerSi}, {ThirdPlacerSi}, {LastPlaceSi}")