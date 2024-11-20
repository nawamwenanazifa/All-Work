# Assignment operators
sum=0
x=0
x=x+5
sum=0+5
sum=5
mult=5
mult=mult+5
mult5*5
mult=25

# given that we have two products a laptop and a mouse such that the price of a laptop is 300000 and the price of a mouse is 50000 use a four loop to find the total sum of the  product

laptop = 300000
mouse = 50000
sum=0
product_price=[laptop,mouse]
for price in product_price:
    sum+=price
    
laptop=300000
mouse=50000
keyboard=30000
total_cost=[mouse,keyboard,laptop]    
print(f"The total sum of the product is: {sum:,}")
total_cost+=laptop
total_cost+=mouse
total_cost+=keyboard
print(f"the total cost of your shoppig cart is UG{total_cost}")
