from datetime import datetime


def task_tracker(message):
    words = message.split(' ')
    iD = len(tasks) + 1
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    if "add" in words:
        message = message.replace("add", "")
        message = " ".join(message.split())
        tasks.append({"id": iD, "description": message, "status": "todo", "CreatedAt": formatted})
        print(f"Task added successfully (ID: {iD})")
    elif "update" in words:
        message = message.replace("update", "").replace(words[1], "")
        message = " ".join(message.split())
        for x in tasks:
            if int(words[1]) == x["id"]:
                x["UpdatedAt"] = formatted
                x["description"] = message
    elif "delete" in words:
        i = int(words[1]) - 1
        tasks.pop(i)
    elif message == "list":
        for item in tasks:
            print(item)
    elif "mark-in-progress" in words:
        for x in tasks:
            if int(words[1]) == x["id"]:
                x["status"] = "in-progress"
    elif "mark-done" in words:
        for x in tasks:
            if int(words[1]) == x["id"]:
                x["status"] = "done"
    elif "list" in words and "done" in words:
        for x in tasks:
            if x["status"] == "done":
                print(x)
    elif "list" in words and "todo" in words:
        for x in tasks:
            if x["status"] == "todo":
                print(x)
    elif "list" in words and "in-progress" in words:
        for x in tasks:
            if x["status"] == "in-progress":
                print(x)
    else:
        print("input a valid task")

tasks = []
is_running = True

while is_running:

    message = input("> ")
    if message == "quit":
        break
    task_tracker(message)
