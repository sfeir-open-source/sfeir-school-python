# -*- coding: utf-8 -*-

"""
To-Do application
"""

import os
import pickle

DONE = '✔'
FILENAME = 'todo.db'


def add(todos):
    """
    Add a task
    """
    task = input('\nNew task: ')
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
    printable_todos = []

    for todo in todos:
        if todo['done']:
            printable_todos.append('{} {}'.format(DONE, todo['task']))
        else:
            printable_todos.append('  {}'.format(todo['task']))

    return printable_todos

def load():
    """
    Load todos from file
    """
    try:
        file = open(FILENAME, 'rb')
        data = pickle.load(file)
        file.close()
        return data
    except IOError:
        return []

def save(todos):
    """
    Save todos to file
    """
    file = open(FILENAME, 'wb')
    pickle.dump(todos, file)
    file.close()

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

    for idx, entry in enumerate(entries):
        tick = '  '

        if index is not None and idx == index:
            tick = '> '

        print('{} {}'.format(tick, entry))


def main():
    """
    Main function
    """
    choice = None
    index = 0
    todos = load()

    while choice != 'q':
        view(todos, index)

        print('\n' + '=' * 40 + '\n')
        print('Previous/Next: p/n\n')

        print('1. Add')
        print('2. Toggle done')
        print('3. Delete')
        print('4. Delete all')
        print('q. Quit')

        choice = input('\nAction: ')

        if choice == '1':
            add(todos)
        elif choice == '2':
            toggle_done(todos, index)
        elif choice == '3':
            delete(todos, index)
            index = 0
        elif choice == '4':
            delete(todos)
            index = 0
        elif choice == 'n' and index < len(todos)-1:
            index += 1
        elif choice == 'p' and index > 0:
            index -= 1

    save(todos)


if __name__ == '__main__':
    main()
