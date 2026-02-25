#ask customer for details
name=input("Enter customer name")

#quantity 
quantity=int(input("enter quantity of coffee"))

price_per_coffe=float(input("enter price per coffee"))

#calculate before tax
subtotal=quantity*price_per_coffe

#calculate 5% tax
tax=subtotal*price_per_coffe


#total
total=subtotal+tax

print(f"Thank you,{name}! Your total for {quantity}coffee,including tax is Rs{total:2f}")