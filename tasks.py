"""Минимальный CLI-менеджер задач."""

tasks = []


def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Задача добавлена: {title}")


def list_tasks():
    if not tasks:
        print("Задач нет")
        return
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['title']}")

def complete_task(index):
    """Пометить задачу с индексом index как выполненную."""
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
