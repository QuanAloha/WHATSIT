"""
This file is used to test small bits of code. It is an experimental space.
"""


def collect_ingredient_list():
    """
    Ask the user to input the ingredients in a certain product from the top of the list to the bottom. Once the user is
    done inputting the information, then they will be move on to the next step of the process.

    :return:
    """
    # Set up the function to work.
    finished_ingredient_input = False
    ingredient_list = []

    while not finished_ingredient_input:
        # Ask the user to input one ingredient.
        ingredient = input('Please type the next ingredient for this product     ')
        ingredient_list.append(ingredient)

        # Check if the user is finished.
        user_done = input('Are there more ingredients to add? (y/n)     ')
        if user_done == 'n' or user_done == 'no':
            finished_ingredient_input = True

    return ingredient_list


def main():
    ingredient_list = collect_ingredient_list()
    print(ingredient_list)


if __name__ == "__main__":
    main()