'''
Author: Logan Maupin
Date: 10/18/2023 

Just a collection of functions you can use to analyze the data 
from those text transcription files.
'''
import matplotlib.pyplot as plt


def extract_text_from_file(filename: str) -> str:
    '''
    This function takes all the text from a txt file and returns a string of it all.

    Parameters:
    filename: str of the name of txt file you wish to extract text from

    Returns: str containing all the text from the text file unmodified in any way.
    '''

    file_txt = ''
    with open(filename, 'r') as txtfile:
        for line in txtfile:
            file_txt += line

    return file_txt


def strip_words(input_string):
    return [word.strip() for word in input_string.split()]


def build_word_set(input_string: str) -> set[str]:
    '''
    This function takes an input string, splits it, sorts it, converts it 
    to a set, and then returns that set. It also removes any non-alpha characters.

    Parameters:
    input_string: any string (preferably with words lol)

    Returns: a sorted set of the string which contains no special chars other than
    a hyphen symbol and will be only the unique words in that set. 
    '''

    # first let's split the string into a list of words
    split_string = input_string.split()

    # next let's remove the whitespace from the strings in that list.
    for word in split_string.copy():

        # I noticed a lot of single letter "words" that aren't right, so
        # let's remove those too while we're at it.
        if len(word) == 1 and word not in ['a', 'i']:
            split_string.remove(word)

        # while we're in here, let's just remove all non letter characters
        for character in word:
            if not character.isalpha() and character != "-":
                character = ''

    # now let's sort the list and the convert it to a set. 
    sorted_set_of_words = set(sorted(split_string))

    return sorted_set_of_words


def build_unique_word_dictionary(input_string: str) -> dict[str, int]:
    '''
    This function will take a string, identify only the unique words, 
    then count how many times those words appeared in the original string.

    Parameters: 
    input_string: any string you wish to count the unique words in

    Returns: dictionary where the keys are the unique words and the
    values are the times those words were found in the string. 
    '''

    unique_word_set = build_word_set(input_string=input_string)

    unique_word_count_dict = {}

    for word in unique_word_set:
        unique_word_count_dict[word] = input_string.count(word)

    return unique_word_count_dict


def extract_only_actual_words(input_string: str, list_of_actual_words: list[str]) -> str:
    '''
    This function takes a word list of known real words and compares it to transcription
    words to make sure the transcription is actually using real words. 

    Parameters: 
    input_string: any string you wish to clear non-real words out of.

    Returns: input_string with only legit words
    '''
    return ' '.join([word for word in input_string.strip() if word in list_of_actual_words])


def word_dictionary_real_word_extraction(word_dict: dict[str, int], valid_words: list[str]) -> dict[str, int]:
    '''
    This function uses a list comprehension to return a new copy of the word dictionary
    with only real legit words in it. (This is necessary for transcription text
    because sometimes the transcription likes to just record sounds that aren't real
    words).

    Parameters:
    word_dict: a dictionary where the keys are unique words and the values are
    the number of times those words appear in the original string.
    valid_words: a list of strings of valid words to check the words against.

    Returns: a new dictionary with only valid word keys
    '''
    valid_word_dict = {}

    for word, count in word_dict.items():
        if word in valid_words:
            valid_word_dict[word] = count

    return valid_word_dict


def plot_words(word_dict: dict[str, int], filename: str) -> None:
    '''
    The purpose of this function is to plot the unique word counts 
    mainly just for my own amusement. (lol)

    Parameters:
    word_dict: a dictionary object of words where the keys are the unique words 
    from a given input_string and the values are the amount of times those words are
    found in the input_string. 
    filename: name of the file as a string, this is used for the chart title

    Returns: None
    '''
    
    words = word_dict.keys()
    counts = word_dict.values()
    # Sort the dictionary by values (word counts) in descending order and take the top 50
    top_words = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:50][::-1]

    # Separate the top words and their counts
    words, counts = zip(*top_words)

    # Create a bar chart
    plt.figure(figsize=(16, 10))  # Adjust the figure size as needed
    plt.barh(words, counts)
    plt.title(f'50 Most Spoken Words in \"{filename.replace(".txt", "")}\"')
    plt.xlabel('Word Frequency')
    plt.ylabel('Words')

    # Add data labels
    for i, count in enumerate(counts):
        plt.text(count, i, str(count), va='center', fontsize=10)

    plt.tight_layout()
    plt.show()


def main():

    ### If you wish to get text data from a YT video (transcription), 
    ### then please use the transcribe_a_video_and_save_to_txt.py file,
    ### that I made for your use case.

    txt_file = input("Please input the filename of the file you wish to plot text data from: \n")

    # if you get file not found errors, make sure the file is in the same directory
    # as this python script, or try using absolute filepaths instead.
    extracted_text = extract_text_from_file(filename=txt_file)

    real_word_list = extract_text_from_file("words_alpha.txt").strip().split()

    word_dict = build_unique_word_dictionary(extracted_text)

    word_dict = word_dictionary_real_word_extraction(word_dict=word_dict, valid_words=real_word_list)

    plot_words(word_dict=word_dict, filename=txt_file)


if __name__ == "__main__":
    main()
