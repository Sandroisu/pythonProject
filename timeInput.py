import datetime

try:
    time = int(input("Введите время в секундах"))
    print(datetime.timedelta(seconds=time))
except:
    print("Вы ввели не число")

