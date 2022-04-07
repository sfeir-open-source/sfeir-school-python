# -*- coding: utf-8 -*-

"""
To-Do application
"""

def concat(input_1, input_2):
    if type(input_1) != type(input_2):
        raise Exception("Concat is not possible")

    print(input_1 + input_2)

def main():
    """
    Main function
    """
    concat("input_1", "input_2")
    try:
        concat(1, "input_2")
    except Exception:
        pass
    concat(["a"], ["b"])


if __name__ == '__main__':
    main()
