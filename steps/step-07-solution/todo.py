# -*- coding: utf-8 -*-

"""
TO-Do class
"""

import os
import pickle


class Todo(object):
    """
    To-Do
    """
    DONE = '✔'

    def __init__(self, task, done=False):
        self.task = task
        self.done = done

    def toggle(self):
        """
        Toggle To-Do state
        """
        self.done = not self.done

    def __str__(self):
        """
        To-Do representation
        """
        if self.done:
            return '{} {}'.format(Todo.DONE, self.task)
        return '  {}'.format(self.task)


class TodoManager(object):
    """
    To-Do manager
    """
    FILENAME = 'todo.db'

    def __init__(self):
        self.todos = []
        self._load()

    def __enter__(self):
        self._load()
        return self

    def __exit__(self, type, value, traceback):
        self._save()

    def add(self):
        """
        Add a task
        """
        task = input('\nNew task: ')
        self.todos.append(Todo(task))

    @staticmethod
    def clear():
        """
        Clear the terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def delete(self, index=None):
        """
        Delete one or all tasks
        """
        if index is not None:
            del self.todos[index]
        else:
            del self.todos[:]

	def _load(self):
		"""
		Load todos from file
        """
    	try:
            file = open(TodoManager.FILENAME, 'rb')
            self.todos = pickle.load(file)
            file.close()
        except IOError:
            self.todos = []

    def _save(self):
        """
        Save todos to file
        """
        file = open(TodoManager.FILENAME, 'wb')
        pickle.dump(self.todos, file)
        file.close()
	
    def toggle_done(self, index):
        """
        Toggle a task
        """
        self.todos[index].toggle()

    def view(self, index):
        """
        Print tasks
        """
        TodoManager.clear()

        print('\nTo-Do list')
        print('=' * 40)

        for idx, entry in enumerate(self.todos):
            tick = '  '

            if index is not None and idx == index:
                tick = '> '

            print('{} {}'.format(tick, entry))

    def __len__(self):
        return len(self.todos)
