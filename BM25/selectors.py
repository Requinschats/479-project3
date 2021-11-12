import math
import os
from pathlib import Path

from naive_indexer import select_doc_id, select_tokenized_array


def select_term_frequency_in_doc(document):
    frequencies = {}
    for term in document:
        term_count = frequencies.get(term, 0) + 1
        frequencies[term] = term_count
    return frequencies


def select_updated_document_frequency(current_document_frequency, frequencies):
    for term, _ in frequencies.items():
        current_document_frequency[term] = current_document_frequency.get(term, 0) + 1
    return current_document_frequency


def select_BM25_initial_values_from_corpus(corpus):
    term_frequency, document_frequency, inverse_document_frequency = [], {}, {}
    total_doc_length, corpus_size = [], 0
    for doc_id, document in corpus:
        corpus_size += 1
        total_doc_length.append(len(document))
        frequencies = select_term_frequency_in_doc(document)
        term_frequency.append(select_term_frequency_in_doc(document))
        document_frequency = select_updated_document_frequency(document_frequency, frequencies)
    return corpus_size, total_doc_length, frequencies, term_frequency, document_frequency


def select_inverse_document_frequency(corpus_size, frequency):
    return math.log(1 + (corpus_size - frequency + 0.5) / (frequency + 0.5))


def select_average_doc_length(total_doc_length, corpus_size):
    return sum(total_doc_length) / corpus_size


def select_BM25_numerator(BM25, term, frequency):
    return BM25.inverse_document_frequency[term] * frequency * (BM25.k1 + 1)


def select_BM25_denominator(BM25, frequency, index):
    return frequency + BM25.k1 * (1 - BM25.b + BM25.b * BM25.total_doc_length[
        index] / BM25.average_doc_length)


def select_query_scores(get_query_score, query, corpus):
    scores = [get_query_score(query, doc_index, doc_id) for doc_index, (doc_id, _) in
              enumerate(corpus)]
    return list(reversed(sorted(scores)))


def select_tokenized_reuters21578_document_list():
    doc_id_tokenized_documents_list = []
    for file_name in os.listdir("reuters21578"):
        file_content = Path('reuters21578/' + file_name).read_text()
        doc_id = select_doc_id(file_content)
        tokenized_content = select_tokenized_array(file_content)
        doc_id_tokenized_documents_list.append((doc_id, tokenized_content))
    return doc_id_tokenized_documents_list
