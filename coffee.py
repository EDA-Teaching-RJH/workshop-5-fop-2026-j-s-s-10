# Statement of Requirements
# Takes at least 75p
# Takes 50p, 20p, 10p and 5p coins
# Input of 1-4 accepted, each number correlates to a coin value
# If other value is input, uses try/except to catch it
# Prints the amount due each time a coin is paid
# If more than 75p is paid, prints change due

paying = True
print("Enter at least 75p")
money = 0
while paying:
    print(f"Amount due: {75 - money}p")

    coin_type = 0
    try:
        coin_type = int(input("Enter coin: 1-50p  2-20p  3-10p  4-5p :: "))
    except:
         print("Invalid input, try again")

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
