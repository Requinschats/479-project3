import os
from pathlib import Path
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def select_tokenized_document(string_document):
    return RegexpTokenizer(r'\w+').tokenize(string_document)


def select_file_content(file_name):
    return Path('reuters21578/' + file_name).read_text()


def select_token_list():
    token_list = []
    for file_name in os.listdir("reuters21578")[:5]:
        file_content = select_file_content(file_name)
        tokenized_content = select_tokenized_document(file_content)
        token_list += tokenized_content
    return token_list


def select_token_set():
    token_set = set()
    for file_name in os.listdir("reuters21578")[:5]:
        file_content = select_file_content(file_name)
        tokenized_content = select_tokenized_document(file_content)
        for token in tokenized_content:
            token_set.add(token)
    return token_set


def select_token_list_without_numbers(token_list):
    return list(filter(lambda token: not token.isdigit(), token_list))


def select_lower_case_token_list(token_list):
    return set(map(lambda token: token.lower(), token_list))

def select_token_list_without_stop_words(token_list):
    english_stopwords = stopwords.words("english")
    return list(filter(lambda string: string not in english_stopwords, token_list))


def select_stemmed_token_list(token_list):
    stemmer = PorterStemmer()
    return list(map(lambda string: stemmer.stem(string), token_list))


def output_distinct_term_stats():
    token_list = select_token_set()
    print("\n -- Distinct terms -- ")
    print("Unfiltered: " + str(len(token_list)))

    token_list_without_numbers = select_token_list_without_numbers(token_list)
    print("No numbers: " + str(len(token_list_without_numbers)))

    token_list_lower_case = select_lower_case_token_list(token_list_without_numbers)
    print("Case folding: " + str(len(token_list_lower_case)))

    token_list_without_stop_words = select_token_list_without_stop_words(token_list_lower_case)
    print("Without stop words: " + str(len(token_list_without_stop_words)))

    token_list_stemmed = select_stemmed_token_list(token_list_without_stop_words)
    print("Stemming: " + str(len(token_list_stemmed)))

#Assumption Posting list means duplicate entries count. Rest will be treated the same
def output_non_positional_stats():
    token_list = select_token_list()
    print("\n -- Nonpositional postings stats -- ")
    print("Unfiltered: " + str(len(token_list)))

    token_list_without_numbers = select_token_list_without_numbers(token_list)
    print("No numbers: " + str(len(token_list_without_numbers)))

    # does not changes if duplicate entries matter (premise on top)
    print("Case folding: " + str(len(token_list_without_numbers)))

    token_list_without_stop_words = select_token_list_without_stop_words(token_list_without_numbers)
    print("Without stop words: " + str(len(token_list_without_stop_words)))

    token_list_stemmed = select_stemmed_token_list(token_list_without_stop_words)
    print("Stemming: " + str(len(token_list_stemmed)))


output_distinct_term_stats()
output_non_positional_stats()