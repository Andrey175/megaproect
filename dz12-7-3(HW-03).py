money = input("Введите сумму которую планируете положить под проценты: ")    
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
b = list(per_cent.values())
deposit = []
deposit.append(float(money) * b[0] / 100)
deposit.append(float(money) * b[1] / 100)
deposit.append(float(money) * b[2] / 100)
deposit.append(float(money) * b[3] / 100)
print("Максимальная сумма, которую вы можете заработать: ", max(deposit))
