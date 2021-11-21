def PengeNgIyongNumero():
    NumeroUno = int(input("Enter the first number you wish to sort: "))
    NumeroDos = int(input("Enter the second number you wish to sort: "))
    NumeroTres = int(input("Enter the third number you wish to sort: "))
    NumeroKwatro = int(input("Enter the fourth number you wish to sort: "))
    return NumeroUno, NumeroDos, NumeroTres, NumeroKwatro


def SortingTime():
    SinoBaPinakaMataas = max(Una, Pangalawa, Pangatlo, Ikaapat)


    if Pangalawa > Una:
        PinakamababaSi = Una
        SecondSi = Pangalawa
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


    print (f"So, from highest to lowest, the arrangement of the list is {PinakamataasSi}, {PangatloSi}, {SecondSi}, {PinakamababaSi}")



Una, Pangalawa, Pangatlo, Ikaapat = PengeNgIyongNumero() 


PakiArrange = SortingTime()