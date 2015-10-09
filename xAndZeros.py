def checkio(game_result):

    col1 = []
    col2 = []
    col3 = []

    diagLR = []
    diagRL = []

    count = 0

    for row in game_result:
        if row == "XXX": return "X"
        elif row == "OOO" : return "O"

        else:
            col1.append(row[0])
            col2.append(row[1])
            col3.append(row[2])

            diagLR.append(row[count])
            diagRL.append(row[2-count])

            count += 1

    if "".join(col1) == "XXX" : return "X"
    elif "".join(col1) == "OOO" : return "O"

    if "".join(col2) == "XXX" : return "X"
    elif "".join(col2) == "OOO" : return "O"

    if "".join(col3) == "XXX" : return "X"
    elif "".join(col3) == "OOO" : return "O"

    if "".join(diagLR) == "XXX" : return "X"
    elif "".join(diagLR) == "OOO" : return "O"

    if "".join(diagRL) == "XXX" : return "X"
    elif "".join(diagRL) == "OOO" : return "O"

    else : return "D"
