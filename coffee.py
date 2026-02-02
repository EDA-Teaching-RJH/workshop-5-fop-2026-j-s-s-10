# Statement of Requirements
# Takes at least 75p
# Takes 50p, 20p, 10p and 5p coins
# Input of 1-4 accepted, each number correlates to a coin value
# If other value is input, uses try/except to catch it
# Prints the amount due each time a coin is paid
# If more than 75p is paid, prints change due

def pay_coin():
    coin_type = 0
    try:
        coin_type = int(input("Enter coin: 1-50p  2-20p  3-10p  4-5p :: "))
    except:
        print("Invalid input, try again")

    return coin_type


def update_total(money, coin_type):
    match coin_type:
        case 1:
            money += 50
        case 2:
            money += 20
        case 3:
            money += 10
        case 4:
            money += 5

    return money


def amount_due(money):
    return f"Amount due: {75 - money}"


def dispense_product(money):
    calculate_change(money)


def calculate_change(money):
    amount_due = money - 75
    coins = []

    while amount_due > 0:
        if amount_due >= 50:
            coins.append("50p")
            amount_due -= 50
        if amount_due >= 20:
            coins.append("20p")
            amount_due -= 20
        if amount_due >= 10:
            coins.append("10p")
            amount_due -= 10
        if amount_due >= 5:
            coins.append("5p")
            amount_due -= 5

    print("Dropping coins: ", end = "")
    for i in coins:
        print(f"{i}, ", end = "")
    print()


def main():
    money = 0
    while money < 75:
        print(amount_due(money))
        money = update_total(money, pay_coin())
    dispense_product(money)


main()
