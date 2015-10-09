def checkio(data):
    outList = []
    for x in data :
        if (data.count(x) > 1) :  outList.append(x)
    return outList