# -*- coding: utf-8 -*-

"""
To-Do application
"""


def add(todos):
    """
    Add a task
    """
    task = input('New task: ')
    todos.append({
        'task': task,
        'done': False
    })

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
    pass

def toggle_done(todos, index):
    """
    Toggle a task
    """
    todos[index]['done'] = not todos[index]['done']

def view(todos, index):
    """
    Print tasks
    """
    print('\nTo-Do list')
    print('=' * 40)


def main():
    """
    Main function
    """
    todos = []

    print('Add New tasks...')
    add(todos)
    add(todos)
    add(todos)
    print(todos)

    print('\nThe Second one is toggled')
    toggle_done(todos, 1)
    print(todos)

    print('\nThe last one is removed')
    delete(todos, 2)
    print(todos)

    print('\nAll the todos are cleaned.')
    delete(todos)
    print(todos)


if __name__ == '__main__':
    main()
