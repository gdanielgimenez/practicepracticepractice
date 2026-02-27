# simple calculator to calculate MB to G

flag = True
while flag:
    print(f" please select what operation you want to do")
    operation = input("1 for Mb to Gb and 2 for Gb to Mb : ")
    if operation == "1":
        mb = float(input("please type in the value in megabytes : "))
        print(f"{mb} megabytes equals to : ")
        gb = mb / 1024
        print(f"{gb:.2f} gigabytes")
        flag = False
    elif operation == "2":
        gb = float(input("please type in the value in Gigabytes : "))
        print(f"{gb} gigabytes equals to : ")
        mb = (gb * 1024)
        print(f"{mb} Megabytes")
        flag = False
    else:
        print("please type in a valid option")
