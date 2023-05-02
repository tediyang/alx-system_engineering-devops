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
        response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(self.employee_id))
        response_dict = response.json()
        return response_dict['name']

    def _get_employee_tasks(self):
        """
        Retrieves the tasks of the employee with the initialized ID.
        """
        response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(self.employee_id))
        response_list = response.json()
        return response_list

    def display_progress(self):
        """
        Displays the employee TODO list progress in the specified format.
        """
        total_tasks = len(self.tasks)
        done_tasks = sum(1 for task in self.tasks if task['completed'])
        print('Employee {} is done with tasks({}/{}):'.format(self.name, done_tasks, total_tasks))
        for task in self.tasks:
            if task['completed']:
                print('\t {} {}'.format(task['title'], '(completed)'))

    def export_csv(self):
        """
        Exports the employee TODO list progress in CSV format with the file name being the employee ID.
        """
        with open('{}.csv'.format(self.employee_id), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
            for task in self.tasks:
                writer.writerow([task['userId'], self.name, task['completed'], task['title']])

        print('CSV file generated: {}.csv'.format(self.employee_id))




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} employee_id'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list = TodoList(employee_id)
    todo_list.display_progress()


    # Validate the number of tasks in the CSV file
    with open('{}.csv'.format(employee_id)) as csvfile:
        reader = csv.DictReader(csvfile)
        task_count = sum(1 for row in reader)
        print('Number of tasks in CSV: {}'.format(task_count))
