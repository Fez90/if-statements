cars=['chevrolet','bmw','subaru','ford']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())    
        
#  conditional tests expressions in if statement that can be evaluated True or False whether code in the if statement should be executed
car = 'bmW'
if car.lower() == 'bmw':
    print("True")
else:
    print("False")    
    
# = sets value, == means equal
# capitalization is different in ana example above so if statement return False that why we use lower case

# inequality operator != represents "not"
requested_toping='mushrooms'
if requested_toping !='anchovies':
    print("Hold anchovies")
answer=17
if answer!=42:
    print("that is not correct answer. Please try again")   
    
# multiply conditions
age_0=21
age_1=18
(age_0>21) and (age_1>21)
(age_0>21) or (age_1>21)

# and function and or function
pizza_toppings=['mushrooms','onions','pineapple']
'mushrooms' in pizza_toppings
# True
'pepperoni' in requested_toping
# False
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")
    
# checking a value is not in the list Python return True and executes the indented line

# Boolean expression is either True or False, often use to keep track of certain condition such as game is running or whether a user can edit certain content on website
game_active=True
can_edit=False


# if elif else statement
age =65
if age<4:
    price = 0
elif age <18:
    price = 25
elif age <65:
    price =40
elif age >=65:
    price = 20
print(f"\nYour admission cost is ${price}")   

# sometimees is better to use if statement instead of if elf else, when more than one condition could be True
requested_toppings=['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza") 

# if statements and lists
toppings = ["pepperoni",'green peppers','extra cheese']
for topping in toppings:
    print(f"Adding {topping} to your pizza")
print("Your order is ready\n")

# example using if statement
pizza_toppings = ['pepperoni','green peppers','extra cheese']
for pizza_topping in pizza_toppings:
    if pizza_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {pizza_topping}")
print("Your order is ready\n")

# checking if list is empty
topings_forpizzas=[]
if topings_forpizzas:
    for topings_forpizza in topings_forpizzas:
        print(f"Adding {topings_forpizza}")
    print("Pizza is ready\n")
else:
    print("Are you sure you want plain pizza\n")
    
# Python returns False because list si empty and executes else line. To run True need to have at least one item in the list

# Using multiple lists
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
customer_toppings = ['mushrooms','french fries','extra cheese']
for customer_topping in customer_toppings:
    if customer_topping in available_toppings:
        print(f"Adding {customer_topping}")
    else:
        print(f"Sorry, we don't have {customer_topping}")
print("\nFinished making your pizza")            