
tasks = []

def main():
    message = """
    1- add tasks to list
    2-mark tasks to completed
    3-view tasks
    4-quit 
    """
    

    while True:
        print(message)
        choice = input("Enter your choice : ")
        if choice == '1':
            # 1- add tasks to list
            add_task()
        elif choice =='2':
            # 2- mark tasks as complete
            mark_complete()
        elif choice =='3':
            # 3- view all tasks
            view_all_tasks()
        elif choice =='4':
            # 4- quit the program
            break
        else:
            print('Invalid Choice')
def add_task():
    # add task to tasks
    task = input("add task: ")
    # difline task status
    task_info = {"task": task, "completed": False}
    # add task to the list of taskas
    tasks.append(task_info)
    print("task added ")

def mark_complete():

    # Find incomplete tasks
    incompleted_tasks = [task for task in tasks if task["completed"] == False]
    
    if not incompleted_tasks:
        print("no task please add task")
        return
    # Display incomplete tasks
    for i, task in enumerate(incompleted_tasks):
        print(f"{i+1}- {task['task']}")
        print("-"*30)
    
    try:
        # Get user input for task number
        task_number = int(input("chose the task to complete: "))

        if task_number < 1 or task_number > len(incompleted_tasks):
            print("invalid index, please choose from the available options")
            return
        # Mark task as completed
        incompleted_tasks[task_number - 1]["completed"] = True
    
        # Notify user of completion
        print("the task is completed")
    except ValueError:
        print("invalid input, please enter a number")
def view_all_tasks():
    if not tasks:
        print("No Tasks Please Add Task")
        return
    for i, task in enumerate(tasks):
        #if task["completed"]:
        #    status = "✅"
        #else:
        #    status = "❌"
        status = "✅" if task ["completed"] else "❌"
        print(f"{i+1}- {task['task']} {status}")
        print("-"*30)

main()

