try:
    number = input("Введите число")
    number = int(number) + int(2 * number) + int(3 * number)
    print(number)
except:
    print("Вы ввели не число")
