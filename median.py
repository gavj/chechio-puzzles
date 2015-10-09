def checkio(data):
    data.sort()
    print(data)
    if len(data)%2 != 0 : return data[len(data)/2]
    else: return (data[len(data)/2 - 1] + data[len(data)/2])/2.0
