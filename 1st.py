# Are you looking to sort the sequence of your desired numbers?, my program does that, all you have to do is input 4 numbers, and
# my program will do all the work.  
def PengeNgIyongNumero():
    NumeroUno = int(input("Enter the first number you wish to sort: "))
    NumeroDos = int(input("Enter the second number you wish to sort: "))
    NumeroTres = int(input("Enter the third number you wish to sort: "))
    NumeroKwatro = int(input("Enter the fourth number you wish to sort: "))
    return NumeroUno, NumeroDos, NumeroTres, NumeroKwatro

# This will be the function responsible for sorting your numbers from highest to lowest. We will use the return values below for this 
# function. 
def SortingTime():
    SinoBaPinakaMataas = max(Una, Pangalawa, Pangatlo, Ikaapat)

    # This if/else statement will verify if your second no. is greater than the first. But if "not"
    if Pangalawa > Una:
        PinakamababaSi = Una
        SecondSi = Pangalawa
    # This else statement will execute the opposite value that did not became True on the if statement.    
    else:
        PinakamababaSi = Pangalawa
        SecondSi = Una

    
    if Pangatlo < Pangalawa:
        PangatloSi = SecondSi
        SecondSi = PinakamababaSi
        PinakamababaSi = Pangatlo

    else:
        PangatloSi = Pangatlo

    
    if SecondSi > PangatloSi:
        SecondSi = SecondSi + PangatloSi
        PangatloSi = SecondSi - PangatloSi
        SecondSi = SecondSi - PangatloSi


    if PinakamababaSi > SecondSi:
        PinakamababaSi = PinakamababaSi + SecondSi
        SecondSi = PinakamababaSi - SecondSi
        PinakamababaSi = PinakamababaSi - SecondSi


    if Ikaapat < PangatloSi:
        PinakamataasSi = PangatloSi
        PangatloSi = SecondSi
        SecondSi = PinakamababaSi
        PinakamababaSi = Ikaapat

    else:
        PinakamataasSi = Ikaapat


    if SecondSi > PangatloSi:
        SecondSi = SecondSi + PangatloSi
        PangatloSi = SecondSi - PangatloSi
        SecondSi = SecondSi - PangatloSi


    if PinakamababaSi > SecondSi:
        PinakamababaSi = PinakamababaSi + SecondSi
        SecondSi = PinakamababaSi - SecondSi
        PinakamababaSi = PinakamababaSi - SecondSi


    print (f"So, based on the numbers you entered; from highest to lowest, the arrangement of the list is {PinakamataasSi}, {PangatloSi}, {SecondSi}, {PinakamababaSi}")


# This right here will return the 4 numbers you entered above, they are essential for the effectiveness of the program.
Una, Pangalawa, Pangatlo, Ikaapat = PengeNgIyongNumero() 


# This variable will return all the operations included in SortingTime(), which means all if/else statements are involved. 
PakiArrange = SortingTime()