import re

def checkio(data):
    dig = 0
    car = 0
    up = 0
    low = 0
    if len(data) >= 10:
        for d in data:
            if d.isdigit() : dig = 1
            if d.isupper() : up = 1
            if d.islower() : low = 1
            if d.isalpha() : car = 1

    if dig and car and up and low : return True
    else : return False
