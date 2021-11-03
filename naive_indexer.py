import time

from nltk import RegexpTokenizer
import os
from pathlib import Path
from collections import OrderedDict
from nltk.corpus import stopwords

from outputs import output_computing_time


def select_string_array_without_stop_words(string_array):
    english_stopwords = stopwords.words("english")
    return list(filter(lambda string: string not in english_stopwords, string_array))


def get_between_tokens(string, startToken, endToken, endOffset):
    return string[string.find(startToken) + len(startToken): string.find(endToken) - endOffset]


def select_doc_id(document):
    return int(get_between_tokens(document, 'NEWID="', '<DATE>', 3))


def select_tokenized_array(string):
    string_without_numbers = ''.join([i for i in string if not i.isdigit()])
    return RegexpTokenizer(r'\w+').tokenize(string_without_numbers)


def select_term_doc_id_pair(token, doc_id):
    return token, doc_id


def select_term_doc_id_list(token_array, doc_id):
    token_array_without_stop_words = select_string_array_without_stop_words(token_array)
    return list(map(lambda token: (token, doc_id), token_array_without_stop_words))


def select_term_doc_list_without_duplicates(term_doc_id_list):
    return list(set(term_doc_id_list))


def select_valid_term_length_term_docId_list(term_doc_id_list):
    return filter(lambda local_term_doc_id: len(local_term_doc_id[0]) > 1, term_doc_id_list)


def select_formatted_term_doc_id_list(term_doc_id_list):
    filtered_term_doc_id_list = select_term_doc_list_without_duplicates(term_doc_id_list)
    filtered_term_doc_id_list = select_valid_term_length_term_docId_list(filtered_term_doc_id_list)
    return sorted(filtered_term_doc_id_list)


def select_document_posting_list_from_term_doc_id_list(term_doc_id_list):
    posting_list = {}
    for term_doc_id in term_doc_id_list:
        posting_list[term_doc_id[0]] = term_doc_id[1]
    return posting_list


def select_document_posting_list_from_file_name(file_name):
    file_content = Path('reuters21578/' + file_name).read_text()
    tokenized_content = select_tokenized_array(file_content)
    term_doc_id_list = select_term_doc_id_list(tokenized_content, select_doc_id(file_content))
    formatted_term_doc_id_list = select_formatted_term_doc_id_list(term_doc_id_list)
    return select_document_posting_list_from_term_doc_id_list(formatted_term_doc_id_list)


def merge_posting_lists(global_posting_list, document_posting_list):
    for term, doc_id in document_posting_list.items():
        if term in global_posting_list:
            global_posting_list[term].append(doc_id)
            global_posting_list[term] = sorted(global_posting_list[term])
        else:
            global_posting_list[term] = [doc_id]
    return global_posting_list


def select_global_posting_list(entry_limit):
    start_time = time.time()
    posting_size = 0

    print("Creating Naive Indexer posing list...")
    global_posting_list = {}
    for fileName in os.listdir("reuters21578"):
        if entry_limit and posting_size >= entry_limit:
            output_computing_time("Naive indexer", start_time)
            return

        document_posting_list = select_document_posting_list_from_file_name(fileName)
        global_posting_list = merge_posting_lists(global_posting_list, document_posting_list)
        posting_size += len(document_posting_list)
    sorted_global_posting = dict(OrderedDict(sorted(global_posting_list.items())))
    return sorted_global_posting
