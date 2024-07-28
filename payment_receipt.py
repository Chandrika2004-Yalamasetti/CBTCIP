#details of company and date of receipt
name="                  LOVE IN EVERY SIP"
bold_name="\033[1m" + name +"\033[0m"
address_contact="           Near airport, main road X road\n                contact:5347940984"
x='*'
from datetime import datetime
print(bold_name)
print(address_contact)
print(' *'*30)
print('\t{}\n'.format(datetime.now()))

#details of order 
item1,price1,quantity1="cappuccino",60,1
item2,price2,quantity2="cold coffee",80,1
item3,price3,quantity3="Brewberry",90,1

#printing the order details
print('\tNAME OF ITEM  \t\tQUANTITY\t $ PRICE ')
print('\t{} \t\t{} \t \t $  {}'.format(item1.title(),price1,quantity1))
print('\t{} \t\t{} \t \t $  {}'.format(item2.title(),price2,quantity2))
print('\t{} \t\t{} \t \t $  {}\n'.format(item3.title(),price3,quantity3))
print(' *'*30)

#total price of order
PRICE=" PRICE"
price=price1+price2+price3
print('\t{} \t \t\t\t$  {}'.format(PRICE.title(),price))


# details at bottom of the receipt
print(' *'*30)
name1="                THANKYOU FOR VISITING\n                 HAVE A NICE DAY"
bold_name1="\033[1m" + name1 +"\033[0m"
print(bold_name1)