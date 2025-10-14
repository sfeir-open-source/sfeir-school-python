# Exercise 1: Decorator
# TODO: Create a decorator `log_decorator` that prints "Calling function <function_name>" before executing the function.


# TODO: Apply the decorator to this function
def say_hello():
    """Prints a greeting."""
    print("Hello, Python!")

# Exercise 2: Lambda
def sort_by_age(people):
    """Sorts a list of people (dictionaries) by age."""
    # TODO: Use a lambda function as the key to sort the list by age.
    sorted_people = [] # Replace with your sorted() call
    return sorted_people

# Exercise 3: List Comprehension
def get_even_squares(numbers):
    """Returns a list of squares of even numbers."""
    # TODO: Use a list comprehension to get the squares of even numbers.
    even_squares = [] # Replace with your list comprehension
    return even_squares


if __name__ == "__main__":
    print("--- Exercise 1: Decorator ---")
    say_hello()

    print("\n--- Exercise 2: Lambda ---")
    people_list = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_people_list = sort_by_age(people_list)
    print(f"Sorted list: {sorted_people_list}")

    print("\n--- Exercise 3: List Comprehension ---")
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares_list = get_even_squares(number_list)
    print(f"Squares of even numbers: {even_squares_list}")