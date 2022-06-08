def calculate(first_day_km, goal_km):
    current_kilometers = first_day_km
    day_count = 1
    while current_kilometers < goal_km:
        current_kilometers = current_kilometers * 1.1
        day_count = day_count+1
        print("День №" + str(day_count) + ": " + str(round(current_kilometers, 2)) + "км")
    return str(day_count)

try:
    firstDayKm = int(input("Сколько пробежал в первый день? "))
    goalKm = int(input("Сколько нужно пробежать? "))
    print("Номер дня, на который результат спортсмена составит не менее " + str(goalKm) + " километров - "
          + calculate(firstDayKm, goalKm))
except:
    print("Вы ввели не число")



