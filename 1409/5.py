k = 0
sym = 0
number1 = int(input("Введите число: "))
number2 = int(str(number1)[::-1])
while number2 % 6 == 0:

    if number2 % 2 == 0:
        print("Последняя ваша цифра четная ")
        while number1 != 0:
            sym = sym + number1 % 10
            number1 = number1 // 10
            k += 1
    if sym / 3 == 0:
        print("Сумма ваших чисел делится на 3")
        ##ПОМОГИТЕ