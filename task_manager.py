"""
Менеджер задач
Задача: Создай класс Task, который позволяет управлять задачами (делами).
У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
(выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
выполненных задач и вывода списка текущих (не выполненных) задач.
"""
import datetime

class Task:
    def __init__(self, name: str, description: str, deadline: datetime.date):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def complete(self):
        self.completed = True

    def info(self, separate = '\n'):
        print(f"Задача: {self.name}{separate}"
              f"Описание: {self.description}{separate}"
              f"Срок выполнения: {self.deadline.strftime("%d-%m-%Y")}{separate}"
              f"Задача {'' if self.completed else 'не '}выполнена")

    def status(self):
        print(f"Задача '{self.name}' {'' if self.completed else 'не '}выполнена")

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, name: str, description: str, deadline: datetime.date):
        self.task_list.append(Task(name, description, deadline))

    def complete(self, name: str):
        result = None
        for task_item in self.task_list:
            if task_item.name == name:
                task_item.complete()
                result = task_item
        if result:
            result.status()
        else:
            print(f"Задача '{name}' не найдена")
        return result

    def remove_task(self, name: str):
        i = 0
        removed = False
        while i < len(self.task_list):
            if self.task_list[i].name == name:
                del self.task_list[i]
                removed = True
                continue
            i += 1
        if removed:
            print(f"Задача '{name}' удалена")
        else:
            print(f"Задача '{name}' не найдена")

    def remove_completed(self):
        i = 0
        while i < len(self.task_list):
            if self.task_list[i].completed:
                del self.task_list[i]
                continue
            i += 1

    def show_current_tasks(self, all_task: bool = False):
        for task_item in self.task_list:
            if not task_item.completed or all_task:
                task_item.info(', ')


def main():
    # создаём Менеджер задач
    task_manager = TaskManager()

    # добавляем задачи
    task_manager.add_task("Позвонить родителям",
                          "Позвонить родителям, спросить что купить",
                          datetime.date.today())
    task_manager.add_task("Разработать ТЗ",
                          "Подготовить ТЗ по новому проекту",
                          datetime.date.today() + datetime.timedelta(days=5))
    task_manager.add_task("Провести переговоры",
                          "Провести переговоры по новому проекту",
                          datetime.date.today() + datetime.timedelta(days=7))
    task_manager.add_task("Выполнить ДЗ",
                          "Выполнить домашнее задание к уроку",
                          datetime.date.today() + datetime.timedelta(days=1))
    task_manager.add_task("Сходить в кино",
                          "Сходить в кино на премьеру",
                          datetime.date.today() + datetime.timedelta(days=3))

    # выводим список задач
    print("\nАктивные задачи:")
    task_manager.show_current_tasks()

    # завершаем некоторые задачи
    print("\nЗавершаем две задачи.")
    task_manager.complete("Позвонить родителям")
    task_manager.complete("Выполнить ДЗ")

    # выводим список задач
    print("\nАктивные задачи:")
    task_manager.show_current_tasks()


if __name__ == "__main__":
    main()