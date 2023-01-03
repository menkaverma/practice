# cars=['audi','bmw','subaru','toyota']
# for car in cars:
#     if car=='subaru':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping='mushrooms'
# if requested_topping != 'anchovies':
#     print("hold the anchovies!!!")

# requested_topping=['cheese','butter','macroni','mozirilla']
# print('butter' in requested_topping )

# banned_users=['andrew','carolina','david']
# user='marie'
# if user not in banned_users:
#     print(f"{user.title()},you can post a response if you wish")

# age=17
# if age >=18:
#     print("You are old enought to vote")
#     print("Have you registered to vote yet?")
# else:
#     print("sorry,you are too young to vote")
#     print("Please register to vote as soon as you turn 18!!!")

# age =12
# if age<4:
#     print("Your admission cost id $0")
# elif age<18:
#     print("Your admission cost is $25")
# else:
#     print("Your admission cost is $40")

# requested_toppings=['mushroom','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}")
# print("\nFinishe making your pizza!")

requested_toppings=['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinishe making your pizza!")
