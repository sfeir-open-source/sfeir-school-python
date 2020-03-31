# -*- coding: utf-8 -*-

"""
To-Do application
"""


def add(todos):
    """
    Add a task
    """
    pass

def delete(todos, index=None):
    """
    Delete one or all tasks
    """
    pass

def get_printable_todos(todos):
    """
    Get formatted tasks
    """
    pass

def toggle_done(todos, index):
    """
    Toggle a task
    """
    pass

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
    print('Add New tasks...')
    # TODO Add 3 tasks & print

    print('\nThe Second one is toggled')
    # TODO Toggle the second task & print

    print('\nThe last one is removed')
    # TODO Remove only the third task & print

    print('\nAll the todos are cleaned.')
    # TODO Remove all the tasks & print


if __name__ == '__main__':
    main()
