# Question 6 (Book Sales)
# A bookstore sells a chemistry textbook for $75 but has a discount for bulk
# sales. Quantity discounts are given according to the quantity listed below;
#	5-9 books		5% discount
#	10-19 books:		10% discount
# 	20-49 books:		20% discount
#	50-99 books:		30% discount
#	100 or more:		40% discount
# Write a program that asks the user to enter the number of books purchased.
# The program should display the discount amount and the total purchase
# amount after the discount.

BOOK_PRICE = 75
# Get the number of books
books = int(input("Enter the number of books: "))
purchase_amount = BOOK_PRICE * books
if books >=5 and books <=9:
    discount = purchase_amount * 0.05
elif books >=10 and books <=19:
    discount = purchase_amount * 0.10
elif books >=20 and books <=49:
    discount = purchase_amount * 0.20
elif books >=50 and books <=99:
    discount = purchase_amount * 0.30
else:
     discount = purchase_amount * 0.40
purchase_after_discount = purchase_amount - discount
print("The purchase amount before discount is $",format(purchase_amount,'.2f'), sep='')
print("The discount amount is $",format(discount,'.2f'),sep='')
print("The purchase amount after the discount is $",format(purchase_after_discount,'.2f'), sep='')
