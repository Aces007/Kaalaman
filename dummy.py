User_First_Number = float(input("First Number: "))
User_Second_Number = float(input("Second Number: "))
User_Third_Number = float(input("Third Number: "))
User_Fourth_Number = float(input("Fourth Number: "))

def User_highest(First_Num, Second_Num, Third_Num, Fourth_Num):
    
    if First_Num >= Second_Num and First_Num >= Third_Num and First_Num >= Fourth_Num:
        highest_number = First_Num

    elif Second_Num >= First_Num and Second_Num >= Third_Num and Second_Num  >= Fourth_Num:
        highest_number = Second_Num 

    elif Third_Num >= First_Num and Third_Num >= Second_Num and Third_Num >= Fourth_Num:
        highest_number = Third_Num

    elif Fourth_Num >= First_Num and Fourth_Num >= Second_Num and Fourth_Num >= Third_Num:
        highest_number = Fourth_Num
    
    return highest_number

Highest_Number_User= User_highest(User_First_Number, User_Second_Number, User_Third_Number, User_Fourth_Number)

def User_High(Highest_Number,First_Num, Second_Num, Third_Num, Fourth_Num):

    if Highest_Number == First_Num:
        if Second_Num >= Third_Num and Second_Num >= Fourth_Num:
            high_number = Second_Num
        elif Third_Num >= Second_Num and Third_Num >= Fourth_Num:
            high_number = Third_Num
        elif Fourth_Num >= Second_Num and Fourth_Num >= Third_Num:
            high_number = Fourth_Num
        return high_number
    if Highest_Number == Second_Num:
        if First_Num >= Third_Num and First_Num >= Fourth_Num:
            high_number = First_Num
        elif Third_Num >= First_Num and Third_Num >= Fourth_Num:
            high_number = Third_Num
        elif Fourth_Num >= First_Num and Fourth_Num >= Third_Num:
            high_number = Fourth_Num
        return high_number
    if Highest_Number == Third_Num:
        if First_Num >= Second_Num and First_Num >= Fourth_Num:
            high_number = First_Num
        elif Second_Num >= First_Num and Second_Num >= Fourth_Num:
            high_number = Second_Num
        elif Fourth_Num >= First_Num and Fourth_Num >= Second_Num:
            high_number = Fourth_Num
        return high_number
    if Highest_Number == Fourth_Num:
        if First_Num >= Second_Num and First_Num >= Third_Num:
            high_number = First_Num
        elif Second_Num >= First_Num and Second_Num >= Third_Num:
            high_number = Second_Num
        elif Third_Num >= First_Num and Third_Num >= Second_Num:
            high_number = Third_Num
        return high_number


High_Number= User_High(Highest_Number_User,User_First_Number, User_Second_Number, User_Third_Number, User_Fourth_Number)
   
def User_lowest(First_Num, Second_Num, Third_Num, Fourth_Num):
    
    if First_Num <= Second_Num and First_Num <= Third_Num and First_Num <= Fourth_Num:
        lowest_number = First_Num

    elif Second_Num  <= First_Num and Second_Num <= Third_Num and Second_Num  <= Fourth_Num:
        lowest_number = Second_Num 

    elif Third_Num <= First_Num and Third_Num <= Second_Num and Third_Num <= Fourth_Num:
        lowest_number = Third_Num

    elif Fourth_Num <= First_Num and Fourth_Num <= Second_Num and Fourth_Num <= Third_Num:
        lowest_number =Fourth_Num

    return lowest_number

Lowest_Number= User_lowest(User_First_Number, User_Second_Number, User_Third_Number, User_Fourth_Number)

      

def User_Low(lowest_Number,First_Num, Second_Num, Third_Num, Fourth_Num):
    
    if lowest_Number == First_Num:
        if Second_Num <= Third_Num and Second_Num <= Fourth_Num:
            low_number = Second_Num
        elif Third_Num <= Second_Num and Third_Num <= Fourth_Num:
            low_number = Third_Num
        elif Fourth_Num <= Second_Num and Fourth_Num <= Third_Num:
            low_number = Fourth_Num
        return low_number
    if lowest_Number == Second_Num:
        if First_Num <= Third_Num and First_Num <= Fourth_Num:
            low_number = First_Num
        elif Third_Num <= First_Num and Third_Num <= Fourth_Num:
            low_number = Third_Num
        elif Fourth_Num <= First_Num and Fourth_Num <= Third_Num:
            low_number = Fourth_Num
        return low_number
    if lowest_Number == Third_Num:
        if First_Num <= Second_Num and First_Num <= Fourth_Num:
            low_number = First_Num
        elif Second_Num <= First_Num and Second_Num <= Fourth_Num:
            low_number = Second_Num
        elif Fourth_Num <= First_Num and Fourth_Num <= Second_Num:
            low_number = Fourth_Num
        return low_number
    if lowest_Number == Fourth_Num:
        if First_Num <= Second_Num and First_Num <= Third_Num:
            low_number = First_Num
        elif Second_Num <= First_Num and Second_Num <= Third_Num:
            low_number = Second_Num
        elif Third_Num <= First_Num and Third_Num <= Second_Num:
            low_number = Third_Num
        return low_number


low_Number= User_Low(Lowest_Number,User_First_Number, User_Second_Number, User_Third_Number, User_Fourth_Number)

def Order_Arrange():
    print("The highest number is", Highest_Number_User)
    print("Followed by", High_Number)
    print("Then", low_Number)
    print("And the lowest is", Lowest_Number)

Order_Arrange()