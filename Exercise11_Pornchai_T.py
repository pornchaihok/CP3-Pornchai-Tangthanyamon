number = int(input("Please input a number: "))
space = number
for x in range(number):
    space -=1
    print(" "*space,"*"*((x*2)+1))
