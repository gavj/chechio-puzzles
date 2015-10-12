def checkio(number):
    food = number
    minute = 0
    pigeons = 0
    oldPigeons = 0
    oldFood = 0
    while True:
        minute += 1
        oldPigeons = pigeons
        pigeons += minute
        oldFood = food
        food -= pigeons
        newPigeions = pigeons - oldPigeons

        if food == 0:
            return pigeons
        elif food<0:
            if (oldFood-oldPigeons) > 0:return oldPigeons + (oldFood-oldPigeons)
            else: return oldPigeons
