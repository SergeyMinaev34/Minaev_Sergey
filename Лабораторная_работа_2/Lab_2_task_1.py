money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0

while money_capital + salary - spend > 0:
     money_capital = money_capital + salary - spend
     count += 1
     spend = spend * 1.05
print("Количество месяцев, которое можно протянуть без долгов:", count)
