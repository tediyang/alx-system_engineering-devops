#!/usr/bin/python3
"""
This module retrieves and export data tpo CSV file.
"""
import json
import requests
import sys


class TodoList:
    """
    This module retrieves and export data tpo CSV file.
    """

    def __init__(self, employee_id=None):
        """
        Initializes the TodoList object with the given employee ID.
        """
        self.employee_id = employee_id
        self.name = self._get_employee_name()
        self.tasks = self._get_employee_tasks()

    def _get_employee_name(self):
        """
        Retrieves the name of the employee with the initialized ID.
        """
        response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(self.employee_id))
        response_dict = response.json()
        return response_dict['username']

    def _get_employee_tasks(self):
        """
        Retrieves the tasks of the employee with the initialized ID.
        """
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                self.employee_id))
        response_list = response.json()
        return response_list

    def export_to_csv(self):
        """
        Displays the employee TODO list progress in the specified format.
        """
        with open("{}.csv".format(self.employee_id), "w") as f:
            for todo in self.tasks:
                f.write('"{}","{}","{}","{}"\n'.format(
                    self.employee_id,
                    self.name,
                    todo.get("completed"),
                    todo.get("title")))

    def export_to_json(self):
        """
        Export the employee todo tasks to json.
        """
        data = [{"task": todo.get("title"),
                 "completed": todo.get("completed"),
                 "username": self.name} for todo in self.tasks]
        user_data = {"{}".format(self.employee_id): data}
        with open('{}.json'.format(self.employee_id), 'w') as json_file:
            json.dump(user_data, json_file)

    @staticmethod
    def export_to_json_all():
        """
        Export all employees' todo tasks to json
        """
        res_user = requests.get('https://jsonplaceholder.typicode.com/users/')
        res_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')

        users_dict = res_user.json()
        tasks_dict = res_todos.json()
        all_data = {}
        for user in users_dict:
            id = user.get("id")
            all_data[str(id)] = []
            for task in tasks_dict:
                if str(id) == task.get("userID"):
                    all_data[str(id)].append(
                        {"username": task.get("username"),
                         "task": task.get("title"),
                         "completed": task.get("completed")})
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_data, json_file)


if __name__ == '__main__':
    todo_list = TodoList()
    todo_list.export_to_json_all()
