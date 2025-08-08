# Problem Name: Menu Based Action
# Description: User chooses an action from a menu by number (1-4), and you display the task selected.


print("____Main Menu____")
print("1 : Create a new post")
print("2 : View notifications")
print("3 : Send a massage")
print("4 : Logout from account")

try:
    choice = int(input("\nEnter a number(1 to 4):").strip())
    
    match choice:
        case 1:
            print("Your new post has been published successfully.")
        case 2:
            print("You have 7 new notifications.")
        case 3:
            print("Message sent successfully")
        case 4:
            print("You have been logged out.")
        case _:
            print("Invalid choice number.")
            
except ValueError:
        print("Enter a valid number.")