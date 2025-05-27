import random
# Menu of foods in a form of a list 
items = ["Penne Pasta","Pasta Alla Vodka","Pizza","Lasagna","Pasta with Truffle","Risoto","Pasta with Tomato Sauce"]
#Prices for what each main food costs in the form of a list 
item_prices = [12,18,15,11,20,13,10]
#men of sides in a form of a list 
sides = ["Meetballs","Parmesan Cheese","Clams","Oisters","Ceaser Salad","French Fries"]
#prices for what each side costs in the form of a list
flair_prices = [5,3,12,13,10,7]
#set total to 0
total = 0
#forever loop
while True:
#encloses the code that might raise an exception 
    try:
#set variable number of items equal to the input so it can ask a question "Welcome to Wyatt's Restaurant! How many menu items do you need?"
        num_of_items = int(input("Welcome to Wyatt's Restaurant! How many menu items do you need? "))
#specifies houw to hand an exception if it occurs 
    except ValueError:
#display message please type in a number
        print("please type in a number")
#continue the current loop iteration 
        continue
#make a blank list called used
    used = []
#a loop that iterates a specific number of times 
    for i in range(num_of_items):
#randomly generate an item from the menu list
        item = random.choice(items)
#randomly generate a side from the sides list
        side = random.choice(sides)
#an item has been previously owned and show signs of wear

        if item + side in used:
#continue the current loop iteration 
            continue
#add an element to the end of the list and modify the orginal list (dose not return any value)
        used.append(item + side)
#get the index of item in the menu list
        item_price = item_prices[items.index(item)] 
#get the index of side in the sides list
        side_price = flair_prices[sides.index(side)]
#to find total cost add up the item price and side price to find the total 
        total += item_price + side_price
#display message item, side, item price plus side price, and add item price and side price to find total cost 

        print(f'{item} {side}, ${item_price} + ${side_price} = ${item_price + side_price} ')
#display message your total price
    print(f'Your total price is ${total}')
    
    