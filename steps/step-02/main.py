# -*- coding: utf-8 -*-

"""
To-Do application
"""

def main(s: str):
    match s:
        case True:
            print("toto")
        case False:
            print("tata")
        case _:
            print("default")


if __name__ == '__main__':
    main("tata")
    main("toto")
    main("other")
