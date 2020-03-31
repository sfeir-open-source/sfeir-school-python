"""
To-Do application
"""

from todo import TodoManager


def main():
    """
    Main function
    """
    choice = None
    index = 0

    while choice != 'q':
        with TodoManager() as todos:
            todos.view(index)

            print('\n' + '=' * 40 + '\n')
            print('Previous/Next: p/n\n')

            print('1. Add')
            print('2. Toggle done')
            print('3. Delete')
            print('4. Delete all')
            print('q. Quit')

            choice = input('\nAction: ')

            if choice == '1':
                todos.add()
            elif choice == '2':
                todos.toggle_done(index)
            elif choice == '3':
                todos.delete(index)
                index = 0
            elif choice == '4':
                todos.delete()
                index = 0

            elif choice == 'n' and index < len(todos)-1:
                index += 1
            elif choice == 'p' and index > 0:
                index -= 1


if __name__ == '__main__':
    main()
