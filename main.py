"""
App Name: Whats It

App Description: This app is designed to make more specific nutritional facts available to users by scanning the
barcode of any product they find in the store. The app will have 3 main parts. The forst part is going to be the
part of the app that the user uses to scan the barcode and look up information. The second part of the app will be a
place for people to input information.

This main.py file is going to have all the central code for the app.
"""


def separate_information_into_dictionary(file_name):
    """
    Take a file and turn it into a variable that the program can use.

    :param file_name: The information file containing barcode numbers and their corresponding facts.
    :return: A dictionary full of the file information.
    """
    # Open the information into a variable.
    information = open(file_name)
    information_list = information.readlines()

    # Create Dictionary to edit
    information_dictionary = {}

    for line in information_list:
        # Create an item in the dictionary.
        barcode_number = line[0:10]  # The barcode numebr will be the first 10 values of the string.
        product_information = line[10:-1]  # This is all the information after the barcode minus the new line notation.

        information_dictionary[barcode_number] = product_information

    return information_dictionary


def is_item_in_list(barcode_number, information):
    if barcode_number in information:
        return True
    return False


def display_information(item_status, barcode_number, information):
    # Return this if the item searched for is not in the list.
    if not item_status:
        return 'This item is not in our records. Please add it now.'

    return information[barcode_number]


def main():
    # Gather information together
    barcode_number = input('Please type a barcode number')
    information = separate_information_into_dictionary('information.txt')

    # Process information
    item_status = is_item_in_list(barcode_number, information)

    # Print Answer
    print(display_information(item_status, barcode_number, information))


if __name__ == "__main__":
    main()