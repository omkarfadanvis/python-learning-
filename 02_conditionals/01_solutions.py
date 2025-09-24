# score = int(input("Enter your score (0-100): "))
# if score>= 90:
#         print('A')
# elif score>=80:
#         print('B')
# elif score>=70:
#         print('C')

# elif score>=60: 
#         print('D')
# else:
#         print('F')




# fruit = input("Enter a fruit: ")
# color = input("Enter a color: ")

# color = color.capitalize()
# fruit = fruit.capitalize()

# if fruit == "Banana" and color == "Yellow":
#     print("It's a banana! and it's ripe.")
# elif fruit == "Banana" and color != "Yellow":
#     print("It's a banana, but not ripe yet.")
# else:
#     print("It's not a banana.") 

password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short.")
elif len(password) > 20:
    print("Password is too long.")
elif len(password)>= 8 and len(password)<=20:
    print("Password length is just right.")


