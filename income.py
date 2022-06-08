try:
    income = int(input("Введите выручку "))
    costs = int(input("Введите издержки "))
    if income > 0 and costs > 0:
        if income > costs:
            print("Прибыль больше издержек")
            profit = income - costs
            print("Рентабельность выручки равна " + str(profit/income))
            employee = int(input("Введите количество сотрудников "))
            print("Прибыль фирмы в расчёте на одного сотрудника " + str(profit / employee))
        else:
            print("Издержки больше прибыли")

    else:
        print("Число должно быть больше 0")
except:
    print("Вы ввели не число")
