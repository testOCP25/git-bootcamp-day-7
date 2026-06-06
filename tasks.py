"""Минимальный CLI-менеджер задач."""

tasks = []


def add_task(title):
    if not title or not title.strip():
        raise ValueError("Название задачи не может быть пустым")
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


def delete_task(index):
    """Удалить задачу по индексу."""
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Задача удалена: {removed['title']}")
