#!/usr/bin/python3
"""
This module retrieves and export data tpo CSV file.
"""
import requests
import sys


class TodoList:
    """
    This module retrieves and export data tpo CSV file.
    """

    def __init__(self, employee_id):
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
        Export the employee todo tasks to CSV file.
        """
        with open("{}.csv".format(self.employee_id), "w") as f:
            for todo in self.tasks:
                f.write('"{}","{}","{}","{}"\n'.format(
                    self.employee_id,
                    self.name,
                    todo.get("completed"),
                    todo.get("title")))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list = TodoList(employee_id)
    todo_list.export_to_csv()
