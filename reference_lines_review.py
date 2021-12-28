"""
Initial code by David Johnson. This code and derived works may not be posted publicly.

Code finished by Nathaniel Atwood
"""

# Add your critical thinking sentences and example review here.
"""
Critical Thinking Review:
Most of the time, the predeicted score is slightly lower than the actual score. However a there are 2 scores on the 
list where the predicted score is actually higher than the actual score. This means that there are some
words in the dictionary that is throwing off the score. However, I a cannot figure out what those words are. 

A phrase that might offset the score is something like 'I am positive this is a bad film.'

"""

# Add your functions here.
def make_lowercase_lines_from_file(file_name):
    """
    Take a line of text and turn all letters into lowercase letters.

    :param file_name: A text file.
    :return: A long list with all the lines from the original file now in lowercase format.
    """
    file = open(file_name)
    lines = file.readlines()
    lowercase_lines = [None] * len(lines)

    for line_number in range(len(lines)):
        lowercase_lines[line_number] = lines[line_number].lower()

    return lowercase_lines


def make_word_total_value_dict_from_lines(lowercase_string_list):
    """
    Select a string from the list and apply attach it to the rating in a dictionary.

    :param lowercase_string_list: A list of strings that has been run through the make_lowercase_lines_from_file function.
    :return: A dictionary with words and ratings attached to each other.
    """
    rating_dictionary = {}
    for line_number in range(len(lowercase_string_list)):
        # These lines of code run through each phrase.
        split_string = lowercase_string_list[line_number].split()  # Split the line so we can loop through it
        rating_number = split_string.pop(0)  # The pop func get's and delete the value at the index at the same time.
        print('The number assigned to all the values is ', rating_number)  # This is a testing line
        print('This is the string without the rating.    ', split_string)  # This is a testing line

        for key in split_string:
            # This code runs through each word.
            if key in rating_dictionary:
                rating_dictionary[key] = int(rating_dictionary[key]) + int(rating_number)
            else:
                rating_dictionary[key] = rating_number

    return rating_dictionary


def make_word_total_count_dict_from_lines(list_of_lowercase_strings):
    """
    Count how many times each word appears, then return those values in a dictionary.

    :param list_of_lowercase_strings: A list of strings that has been run through the make_lowercase_lines_from_file function.
    :return: a dictionary with matching keys, but this time the values are equal to how many times a word appears.
    """
    total_count_dictionary = {}
    for line_number in range(len(list_of_lowercase_strings)):
        # These lines of code run through each phrase.
        lowercase_string = list_of_lowercase_strings[line_number]
        lowercase_string = lowercase_string[1:]
        split_string = lowercase_string.split()  # Split the line so we can loop through it
        print('This is the string without the rating.    ', split_string)  # This is a testing line

        for key in split_string:
            # This code runs through each word.
            if key in total_count_dictionary:
                total_count_dictionary[key] = int(total_count_dictionary[key]) + 1
            else:
                total_count_dictionary[key] = 1

    return total_count_dictionary


def make_word_avg_value_from_total_and_count(word_total_dict, word_count_dict):
    """
    Use the two dictionaries calculated before to calculate an average score for each word.

    :param word_total_dict: Result from the make_word_total_value_dict_from_lines function
    :param word_count_dict: Result from the make_word_total_count_dict_from_lines function
    :return: A dictionary with an average value of a words rating over how often it shows up.
    """
    average_value_dictionary = {}
    print(len(word_total_dict))  # This is a testing Line
    print(len(word_count_dict))  # This is a testing line
    for key in word_total_dict:
        average_value = int(word_total_dict[key]) / int(word_count_dict[key])
        average_value_dictionary[key] = average_value

    return average_value_dictionary

def predict_review(single_review_string, average_value_dictionary):
    """
    Predict how many stars a reviewer will give based on their description.

    :param single_review_string: A single review from the list of movie reviews.
    :param average_value_dictionary: The Average Value dictionary calculated earlier.
    :return: A Prediction of that rating a certain review description will get.
    """

    split_single_review_string = single_review_string.split()
    sum_word_score = 0
    number_to_divide_by = 0

    for word in split_single_review_string:
        if word in average_value_dictionary:
            sum_word_score += average_value_dictionary[word]
            number_to_divide_by += 1

    print(sum_word_score)
    print(number_to_divide_by)

    predicted_score = sum_word_score / number_to_divide_by

    return predicted_score


def compare_prediction_with_actual(lines, avg_value_dict):
    """
    Given a list of moview reviews and a dictionary of words and their avg value, compare
    the predicted rating with the actual rating.
    :param lines: a list of movie reviews. Each review starts with a 0 to 4 movie rating.
    :param avg_value_dict: A dict of words and their average value in a movie review rating
    :return: None. This prints out some predicted and actual score for movie reviews.
    """
    for line in lines:
        words = line.split()
        actual_score = int(words[0])
        predicted_score = predict_review(" ".join(words[1:]), avg_value_dict)
        print("predicted:", predicted_score, "actual:", line)

def main():
    """
    Read a file of movie reviews, develop a dict of word values, and use
    those to make movie rating predictions.
    """
    # Add some testing code below here. Make a small list of reviews by hand or read in a small
    # file. Make small total value and count dicts to test the avg function. Make a small
    # avg dict to test the prediction function. Make these by hand to make the tests be as independent
    # from each other as possible.

    dakine = make_lowercase_lines_from_file("smallReviews.txt")
    print(dakine)

    word_count = make_word_total_count_dict_from_lines(dakine)
    print(word_count)
    word_total = make_word_total_value_dict_from_lines(dakine)
    print(word_total)

    avg_dict = make_word_avg_value_from_total_and_count(word_total, word_count)
    print(avg_dict)

    print(predict_review("a pretty excellent film", avg_dict))


    # You should not need to change the code below here. You can comment out some of the print statements if
    # they are producing so much text it is confusing.

    # read the reviews into a list
    # lines = make_lowercase_lines_from_file("smallReviews.txt")
    lines = make_lowercase_lines_from_file("MovieReviews.txt") # uncomment this when you are ready to try the full set of reviews.
    print(lines) # examine the result

    # Make a dict with words from reviews and their summed up values from the reviews they are in
    total_value_dict = make_word_total_value_dict_from_lines(lines)
    print(total_value_dict) # examine the dict to see if it looks correct

    # Count up how often a word appears in all the reviews
    total_count_dict = make_word_total_count_dict_from_lines(lines)
    print(total_count_dict) # examine the dict to see if it looks correct

    # Get the average value per word from the total value and their count
    avg_value_dict = make_word_avg_value_from_total_and_count(total_value_dict, total_count_dict)
    print(avg_value_dict) # examine the dict to see if it looks correct

    # Compare actual and predicted movie ratings for a small number of reviews
    if len(lines) < 110:
        compare_prediction_with_actual(lines, avg_value_dict) # use all for small review files
    else:
        compare_prediction_with_actual(lines[100:110], avg_value_dict)

    # Ask the user for a movie review and predict a rating. It should be without punctuation.
    personal_review = input("Please enter a review with no punctuation: ")
    personal_review = personal_review.lower()
    prediction = predict_review(personal_review, avg_value_dict)
    print("The predicted review score is", prediction)

if __name__=="__main__":
    main()
