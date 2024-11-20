# Control flow structure refers to the orders 
#
#
#the programme should print you bought checken if the user bought checken
#the programme should print you bougt liver if the user bought liver
#else you bought fish

food_type = input("Enter the food type bought: ").lower()
if food_type == 'chicken':
    print("You bought chicken from the markek: ")
elif food_type == 'liver':
    print("You bought liver from the market: ")  
else:
    print("You bought fish from the market: ")   
#NB. This approach only prompts the user to enter only chicken or liver , and if the user enter any food type it will print fish

#Approach 2
# if you want to ensure that the user bought chicken, liver or fish
food_type = input("Enter the food type bought: ").lower()
if food_type == 'chicken':
    print("You bought chicken from the markek: ")
elif food_type == 'liver':
    print("You bought liver from the market: ")  
elif food_type  == 'fish':
    print("You bought fish from the market: " )  