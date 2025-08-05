# Simple CLI-based To-Do List Manager
# Author: Shefaul Islam Shefa
# Date: 2025-08-06


todoList = []
print("Welcome to your To-Do list manager")
print("**********************************")
    
while True:
    print("Chose an option:")
    print("To add a task press : 1")
    print("To view all task press : 2")
    print("To remove a task press : 3")
    print("Exit : 4")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            task = input("Enter a task to add: ")
            todoList.append(task)
            print(f"Added: {task}")
        
        elif choice == 2:
            if todoList:
                print("Your current tasks:")
                for i in todoList:
                    print(f"{i}",end = " ")
                print()
            else:
                 print("Your to-do list is empty")   
        
        elif choice == 3:
            if todoList:
                removeTask = input("Enter the task to remove: ")
                if removeTask in todoList:
                    todoList.remove(removeTask)
                    print(f"Remove: {removeTask}")
                else:
                    print("Task not found.")
            else:
                print("Your to-do list is empty.")
                
        elif choice == 4:
            print("Exiting...Have a great day!")
            break
        
        else:
            print("Invalid number. Please enter between 1 and 4")
            
    except ValueError:
        print("Please enter a vlid number (1-4).")