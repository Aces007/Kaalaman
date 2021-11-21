IlistaNyoPo = int
Listahan = []


Ilista = True

while Ilista:
    IlistaMoLahatNgNumeroMo = input("Enter the values you wish to sort: ")
    Listahan.append(IlistaMoLahatNgNumeroMo)
    if IlistaMoLahatNgNumeroMo == ("TaposNa"):
        break
    else:
        print ("Then")

print ("The unsorted lements are: ", Listahan)

i = 0

for i in range(i,len(Listahan)):
    for j in range(i+1, len(Listahan)):
        if Listahan[i] > Listahan[j]:
            temp = Listahan[i]
            Listahan[i] < Listahan[j]
            Listahan[j] = temp


print ("The sorted elements are:", Listahan)