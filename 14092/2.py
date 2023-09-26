popitka = 0
inter = 0
raz = input("Какой интерактив вы хотите?" )
if raz == "game":
    while inter != '5':
        inter = input("Унадай число!" )
        popitka+=1
        if popitka == 3:
            break
            print(" Извини, но ты проиграл")
        if inter == 'off':
            print("Пока!")
            break
    print("Вы выиграли билет на концерт!")
