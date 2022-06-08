try:
    number = input("Введите число")
    if int(number) > 0:
        numbers = list(number)
        biggest = 0
        for numAtIndex in numbers:
            if biggest < int(numAtIndex):
                biggest = int(numAtIndex)
            if biggest == 9:
                break
        print(biggest)
    else:
        print("Число должно быть больше 0")
except:
    print("Вы ввели не число")
