tasks={}
i=1
def add_task():
    global i
    additional=input("\nwhat is the task?\n")
    tasks[i]=additional
    with open("tasksFILE.txt",'a') as f:
        f.write(f"{i}:{additional}\n")
    i+=1
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("------TODO List is emplty-----")
    for key,value in tasks.items():
        print(f"{key}:{value}")

def rem_task():
    deletion=int(input("\nWhich index task you want to delete?"))
    if deletion in tasks:
        del tasks[deletion]
        print("Task removed successfully!")
    else:
        print("Task not found.")

print("CLI TODO\n")

while True:
    print("\n1.View Tasks \n2.Add Task \n3.Remove Task \n4.Exit")
    choice=int(input("What do you want?\n"))
    if choice==1:
        view_tasks()
    elif choice==2:
        add_task()
    elif choice==3:
        rem_task()
    elif choice==4:
        break
    else:
        print("Invalid choice. Please try again.")





