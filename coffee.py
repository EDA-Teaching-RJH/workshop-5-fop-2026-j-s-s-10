paying = True
print("Enter at least 75p")
money = 0
while paying:
    print(f"Amount due: {75 - money}p")

    coin_type = int(input("Enter coin: 1-50p  2-20p  3-10p  4-5p :: "))

    match coin_type:
        case 1:
            money += 50
        case 2:
            money += 20
        case 3:
            money += 10
        case 4:
            money += 5

    if money >= 75:
        paying = False
        print(f"You are owed {money - 75}p change")
