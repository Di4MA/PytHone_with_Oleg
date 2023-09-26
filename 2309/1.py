game = input("в какую настольную игру?")
gameit = [ ]
while game != "0":
    if game in gameit:
        print("Игра записанна")
    else:
        gameit.append(game)
    game = input("в какую настольную игру?")
gameit.sort()
print(gameit)