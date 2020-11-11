usernameInput = input("Username:")
passwordInput = input("Password:")
if usernameInput == "admin" and passwordInput == "admin":
    print("------ Welcome to Pick A Thing Shop ------")
    print("= = = Item list = = =")
    print("Code / Name / Price(THB)")
    print("P1     Fish      30   ")
    print("P2     Egg       10   ")
    print("P3     Duck      20   ")
    chosenproduct = input("Product code:")
    if chosenproduct == "P1":
        quantity = int(input("Quantity:"))
        print(f"Fish x {quantity} ==> Total amount {30 * quantity} THB")
    elif chosenproduct == "P2":
        quantity = int(input("Quantity:"))
        print(f"Egg x {quantity} ==> Total amount {10 * quantity} THB")
    elif chosenproduct == "P3":
        quantity = int(input("Quantity:"))
        print(f"Duck x {quantity} ==> Total amount {20 * quantity} THB")