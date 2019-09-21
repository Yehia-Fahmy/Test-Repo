# program to find the number of coins to give as change

# change that is required in cents
# 33 => 1 quarter, 1 nickle, 3 pennies
we_want = 225


def find_num_coins(change):
    num_coins = 0
    coins = [200, 100, 25, 10, 5, 1]
    for coin in coins:
        x = 0
        x = change / coin
        change -= x * coin
        num_coins += x

    return num_coins


print(find_num_coins(we_want))
