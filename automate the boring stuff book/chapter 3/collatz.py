# the collatz sequence
def collatz(number):
    if number % 2 == 0:
        # do this if number is pair
        print(number//2)
        return number//2
    else:
        # do this if number is odd
        print(3*number+1)
        return 3*1+1


flag = True
while flag:
    number = input("please type an integer number : ")
    try:
        number = int(number)
    except ValueError:
        message = "strings are not numbers"
        print(message)
    else:
        while number != 1:
            number = collatz(number)
        flag = False
