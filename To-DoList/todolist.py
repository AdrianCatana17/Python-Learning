
# Define a function to show the menu
def menu():
    print("Menu:")
    print("1. Display the To-Do List")
    print("2. Add a task")
    print("3. Mark the task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Define a function to show the list
def show_todo_list(todo_list):
    if not todo_list:
        print("The To-Do List is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index}. [{'X' if task["completed"] else " "}] {task["description"]}")

# Define a function to add a task
def add_task(todo_list):
    description = input("Add the task: \n")
    todo_list.append({"description": description, "completed": False})
    print("Task added successfully")

# Define a function to check if the task is completed
def complete_task(todo_list):
    index = int(input("What is the number of the task you wish to mark as completed?: \n"))
    if index < len(todo_list):
        todo_list[index]["completed"] = True
        print("The task was marked as completed")
    else:
        print("Wrong task number")

# Define a function to delete a task
def delete_task(todo_list):
    index = int(input("What is the number of the task you wish to delete?: \n"))
    if index < len(todo_list):
        del todo_list[index]
        print("The task was successfully deleted!")
    else:
        print("Wrong input!")

def main():
    todo_list = []
    
    while True:
        menu()
        choice = input("Make a choice: ")

        if choice == "1":
            show_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Good bye!")
            break
        else:
            print("Wrong choice.")
        
        
        
if __name__ == "__main__":
    main()