#input 
bill_amount=float(input("Enter the total bill amount"))
tip_percentage=float(input("enter the tips percenatge you want to leave"))
num_people=int(input("Enter the number of people splitting the bill"))

#calcualtion
tip_amount=bill_amount*(tip_percentage/100)
total_bill=bill_amount+tip_amount
amount_per_person=total_bill/num_people


#output format of two decimal
print(f"Each person should pay :{amount_per_person:.2f}")