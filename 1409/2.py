resault = int(input("Введите сумму к оплате: "))
now_time = int(input("Введите текущий час: "))
if now_time >10 and now_time <= 12:
    print(resault/2)
elif now_time >= 20 and now_time <= 22:
    print(resault/4)
else:
    print(price)