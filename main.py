tasks = []

while True:
    print("1.Add Task 2.View Tasks 3.Exit")
    ch = input("Choice: ")
    if ch == '1':
        task = input("Task: ")
        tasks.append(task)
    elif ch == '2':
        print(tasks)
    elif ch == '3':
        break
