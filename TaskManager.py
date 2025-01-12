# Менеджер задач
#
# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "не выполнено"

    def mark_as_completed(self):
        self.status = "выполнено"

    def __str__(self):
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f"Задача отмечена как выполненная: {task}")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "не выполнено"]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Сделать уборку", "12-01-2025")
    manager.add_task("Купить продукты", "15-01-2025")

    # Отметка задачи как выполненной
    manager.mark_task_as_completed("Сделать уборку")

    # Вывод списка текущих задач
    manager.list_current_tasks()

