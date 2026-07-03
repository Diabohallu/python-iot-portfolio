
name = input("Enter your name: ").title().strip() # Used input function, title function and strip function
age = int(input("Enter your age: ")) # Used int funtion (Converting Data type)

hobbies = input("Enter your hobbies: ").title().replace(" ", ",").split(",") # Used split function (to split the string into a list) and replace functiton (to replace empty space with commas)
updated_hobbies = input("Do you wanna add or remove a hobby? (add/remove/no): ").lower().strip() # Used lower function 
if (updated_hobbies == "add"): #used if and elif
    add_hobby = input("Enter the new hobby: ").title().strip()
    hobbies.append(add_hobby) # Used append function  
    updated_hobbies = input("Do you wanna add or remove a hobby? (remove/no): ").lower().strip() # Used lower function 
    if (updated_hobbies == "remove"):
        remove_hobby = input("Enter the hobby you want to remove: ").title().strip()
        hobbies.remove(remove_hobby) # Used remove function
elif (updated_hobbies == "remove"):
    remove_hobby = input("Enter the hobby you want to remove: ").title().strip()
    hobbies.remove(remove_hobby) 
    updated_hobbies = input("Do you wanna add or remove a hobby? (add/no): ").lower().strip()
    if (updated_hobbies == "add"): 
       add_hobby = input("Enter the new hobby: ").title().strip()
       hobbies.append(add_hobby) 
len_hobbies = len(hobbies) # Used len function

food = input("Enter your favourite food(s): ").title()
favourite_food = set(food.split(","))
fact = input("Enter one interesting fact about yourself: ").capitalize().strip() # Used capitalize function

print("\nAbout Myself:") # Used print function and \n (for new line)
print("Hello, I am",name) 
print("I am", age,"years old")
print("I have", len_hobbies, "hobbies")
print("My hobby/hobbies is/are", hobbies) 
print("My favourite food(s) is/are", favourite_food)
print("A fact about me is", fact)

user = {     #Made a dictionary to store user information
    "Name": name,
    "Age": age,
    "Hobby/Hobbies": hobbies,
    "Favourite food(s)": favourite_food,
    "A fact about,{name}": fact

}
print("\nUser Information:")
for key, value in user.items():
    print(key,":",value)