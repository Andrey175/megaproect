tickets = int(input("Введите количество билетов: "))
person = tickets
price = 0

while person != 0:
    age_person = int(input(f'Укажите возраст для посетителя билета № {person} ? '))
    if age_person < 18:
        print('Билет бесплатный')
    elif 25 > age_person >= 18:
        price += 990
        print('Стоимость билета: 990 руб.')
    else:
        price += 1390
        print('Стоимость билета: 1390 руб.')
    person -= 1

if tickets > 3:
    sale_price = price - ((price / 100) * 10)
    print(f'За покупку более 3 билетов скидка 10%. Сумма к оплате: {sale_price} руб.')
else:
    print(f'Сумма к оплате: {price} руб.')

