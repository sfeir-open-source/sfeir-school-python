import unittest

from mock import patch

from todo import Todo, TodoManager


class TestTodo(unittest.TestCase):
    def test_default(self):
        todo = Todo('foo')
        self.assertEqual(todo.task, 'foo')
        self.assertFalse(todo.done)
    
    def test_default_done(self):
        todo = Todo('bar', True)
        self.assertEqual(todo.task, 'bar')
        self.assertTrue(todo.done)

    def test_toggle_done(self):
        todo = Todo('baz')
        todo.toggle()
        self.assertTrue(todo.done)


class TestTodoManager(unittest.TestCase):
    def setUp(self):
        patch('todo.TodoManager._load').start()
        patch('todo.TodoManager._save').start()

        self.manager = TodoManager()
        self.manager.todos = [
            Todo('foo'),
            Todo('bar')
        ]

    @patch('builtins.input', return_value='baz')
    def test_add(self, patch_raw_input):
        self.manager.add()
        self.assertEqual(self.manager.todos[2].task, 'baz')

    def test_delete(self):
        self.manager.delete(1)
        self.assertEqual(len(self.manager.todos), 1)

    def test_delete_all(self):
        self.manager.delete()
        self.assertEqual(len(self.manager.todos), 0)

    def test_toggle_done(self):
        self.manager.toggle_done(0)
        self.assertEqual(self.manager.todos[0].done, True)


if __name__ == '__main__':
    unittest.main()
