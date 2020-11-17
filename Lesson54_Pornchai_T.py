def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "customer" and passwordInput == "1234":
        return True
    else:
        print("Username or Password is wrong.")
        print("Please type it again.")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

#Price calculation program

login()
showMenu()
choice = menuSelect()
if choice == 1:
    PriceAfterVat = vatCalculator(int(input("Please input total price: ")))
    print(PriceAfterVat)
elif choice == 2:
     totalPrice = priceCalculator()
     print(totalPrice)
print("Thank you for shopping with us!")


