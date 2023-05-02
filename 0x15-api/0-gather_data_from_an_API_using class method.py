#!/usr/bin/python3
"""
This module retrieves and displays a given employee's TODO list progress.
"""

import requests
import sys


class TodoList:
    """
    This class retrieves and displays a given employee's TODO list progress.
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
        return response_dict['name']

    def _get_employee_tasks(self):
        """
        Retrieves the tasks of the employee with the initialized ID.
        """
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            self.employee_id))
        response_list = response.json()
        return response_list

    def display_progress(self):
        """
        Displays the employee TODO list progress in the specified format.
        """
        total_tasks = len(self.tasks)
        done_tasks = sum(1 for task in self.tasks if task['completed'])
        print('Employee {} is done with tasks({}/{}):'.format(
            self.name, done_tasks, total_tasks))
        for task in self.tasks:
            if task['completed']:
                print('\t {} {}'.format(task['title'], '(completed)'))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list = TodoList(employee_id)
    todo_list.display_progress()