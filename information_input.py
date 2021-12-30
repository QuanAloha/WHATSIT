"""
This code deals with the inprocessing of information for the information.txt file.

In-processing should happen in a couple of steps.
1. The user should be asked if they want to help with the in-processing of the information
2. The user needs to be asked to take a picture of the product.
3. The user will input basic information about a product including the name and manufacturer.
4. The user needs to input the ingredients listed on the side of the product.
        4a. Something cool we could so here is make it possible for the user to take a picture of the ingredients,
        and then the software would be able to make a list of the ingredients in a certain product.
"""


def collect_picture():
    """
    The user needs to photograph the picture, and then then moved on to the next step.

    :return: A picture of the product.
    """
    pass


def collect_basic_information():
    """
    Ask the user to input some basic information about the product like the Product Name,
    :return:
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


def add_item(barcode_number, ingredient_list, contributor_name):
    pass
