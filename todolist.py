# This is a simple to-do list application project using python programming
# this program manages tasks using a list and implements the basic functionalities of adding, removing, and viewing tasks 
# through a simple while loop and if-else conditions. 

tasks = []
while True:
    print("\n~~~~~~~~~~~ TO-DO LIST MENU~~~~~~~~~~~~")
    print("\n1.Add Task")
    print("\n2.Remove Task")
    print("\n3.View Tasks")
    print("\n4.Exit")

    choice =  input("Enter your choice: ")

    if choice == "1":
      task = input("\nEnter your task: ")
      tasks.append(task)
      print("\nTasks added successfully!")

    elif choice == "2":
     if tasks:
        print("\nCurrent Taks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        task_index = int(input("\nEnter the Task you want to remove: "))
        if 1 <= task_index <= len(tasks):
            tasks.pop(task_index -1 )
            print("\nTask removed successfully!")
        else:
            print("\nInvalid index!")
     else:
        print("\nNo tasks to remove!")
    
    elif choice == "3":
     if tasks:
        print("\nTasks:")
        for task in tasks:
            print(task)
     else:
        print("\nNo task to dislplay")    
    
    elif choice == "4":
        print("\n Exiting...")
        break
    
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")

