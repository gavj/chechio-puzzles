def checkio(number):
    checkPoint = {1:"one", 2:"two", 3:"three" ,4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",\
        9:"nine", 10:"ten", 11:"eleven", 12:"twelve" , 13:"thirteen", 14:"fourteen", \
        15: "fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty",\
        60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred",}

    output = ""

    if number in checkPoint and number != 100:
        output = checkPoint[number]

    else:
        hund = number/100
        tensPlace = number%100
        tens = (number%100)/10
        ones = (number%100)%10

        if hund:
            output = checkPoint[hund]+" hundred"

        if tensPlace in checkPoint:
            if output == "":
                output = checkPoint[tensPlace]
            else:
                output = output+" "+checkPoint[tensPlace]
        elif tens:
            if output == "":
                output = checkPoint[tens*10]
            else:
                output = output+" "+checkPoint[tens*10]

        if ones in checkPoint and tensPlace not in checkPoint:
            if output == "":
                output = checkPoint[ones]
            else:
                output = output+" "+checkPoint[ones]

    return output
