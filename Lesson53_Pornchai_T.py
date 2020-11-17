def vat_cal(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

final_result = vat_cal(int(input("Please input total price: ")))
print(final_result)