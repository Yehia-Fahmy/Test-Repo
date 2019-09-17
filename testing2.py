number = input("Input a Number: ")

try:
    value = int(number)
    print("Yes the input is a number!")
    if value < 5:
        print(f"{value} < 5")
    else:
        print(f"{value} > 5")
except ValueError:
    print("No input is not a number :(")

