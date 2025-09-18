print("\n===== To-Do List =====")
def main():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark tasks as done")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            # if(n_tasks<=1):
            #     print("you have not added any task yet...")
            # else:
                print("\nTasks")
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0<= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print(f"{task_index+1} marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

        ch=input("\nDo you want to continue? y/n : ")
        if(ch=='y'):
            continue
        else: 
            break
        
main()