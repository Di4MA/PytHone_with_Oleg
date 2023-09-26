tel = input("Введите свой номер:")
if (tel[0] =='+'):
    tel_reg = tel.replace("+", "")
print('Ваш код оператора',tel[2:5])