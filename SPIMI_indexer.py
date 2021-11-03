import os
import time
from pathlib import Path

from PostingList import PostingList
from naive_indexer import select_tokenized_array, select_string_array_without_stop_words, \
    select_doc_id
from outputs import output_computing_time


def select_global_posting_list(entry_limit=None):
    start_time = time.time()
    print("Creating SPIMI posing list...")

    posting_list = PostingList(entry_limit)
    for file_name in os.listdir("reuters21578"):
        file_content = Path('reuters21578/' + file_name).read_text()
        doc_id = select_doc_id(file_content)
        tokenized_content = select_tokenized_array(file_content)

        posting_list.add_token_array_to_posting(
            select_string_array_without_stop_words(tokenized_content), doc_id)

        if posting_list.has_reached_subproject1_maximum_entries():
            return output_computing_time("SPIMI", start_time)
    return posting_list.values
