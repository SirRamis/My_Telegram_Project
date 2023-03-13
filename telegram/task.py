HELP = """
help - напечатать справку по программе.  
add - добавить задачу в список ( название задачи запрошиваем у пользователя). 
show -напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня"""

RANDOM_TASK = "Записаться на курс в Нетологию"
tasks = {

}

run = True


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на дату ", date)


while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Ввидите дату для отображения спипка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        print(tasks)
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        add_todo("Сегодня", RANDOM_TASK)
        if "Сегодня" in tasks:
            tasks["Сегодня"].append(RANDOM_TASK)
        else:
            tasks["Сегодня"] = []
            tasks["Сегодня"].append(RANDOM_TASK)
    else:
        print("Неизвестная команда")
        run = False

print("До свидания!")
