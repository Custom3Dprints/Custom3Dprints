def Bill_generator(food, drinks, tax_amount, tip_amount):
    Bill_amount = round(food + drinks, 2)
    tax = round(Bill_amount*tax_amount, 2) #rounds the decimal to the second place(hundreth)
    tip = round((Bill_amount + tax) * tip_amount, 2)
    total = round(Bill_amount + tax + tip, 2)
    return ("Cost of Meal:   $   {}\nTax Amount:     $    {}\nTip Amount:     $    {}\
        \n{}\nTotal:          $   {}".format(Bill_amount, tax, tip,"-"*30, total))

print(Bill_generator(float(input("Please enter the cost of food: ")), \
    float(input("Please enter the cost of drinks: ")),  .075, .18)) #calls the function