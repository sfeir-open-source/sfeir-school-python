# -*- coding: utf-8 -*-

"""
To-Do application
"""

def add(input_1, input_2):
    if type(input_1) != type(input_2):
        raise Exception("Concat is not possible")

    return input_1 + input_2

def main():
    """
    Main function
    """
    print(add("input_1", "input_2"))
    try:
        print(add(1, "input_2"))
    except Exception as e:
        print(e)
    print(add(["a"], ["b"]))


if __name__ == '__main__':
    main()
