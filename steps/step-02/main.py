# -*- coding: utf-8 -*-

"""
To-Do application
"""

import os

DONE = '✔'


def add(todos):
    """
    Add a task
    """
    task = input('New task: ')
    todos.append({
        'task': task,
        'done': False
    })

def clear():
    """
    Clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def delete(todos, index=None):
    """
    Delete one or all tasks
    """
    if index is not None:
        del todos[index]
    else:
        del todos[:]

def get_printable_todos(todos):
    """
    Get formatted tasks
    """
    return []

def toggle_done(todos, index):
    """
    Toggle a task
    """
    todos[index]['done'] = not todos[index]['done']

def view(todos, index):
    """
    Print tasks
    """
    clear()
    entries = get_printable_todos(todos)

    print('\nTo-Do list')
    print('=' * 40)


def main():
    """
    Main function
    """
    index = 0
    todos = []

    view(todos, index)

    print('\n' + '=' * 40 + '\n')
    print('Previous/Next: p/n\n')

    print('1. Add')
    print('2. Toggle done')
    print('3. Delete')
    print('4. Delete all')
    print('q. Quit')

    choice = input('\nAction: ')


if __name__ == '__main__':
    main()
