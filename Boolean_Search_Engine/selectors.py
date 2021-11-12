import numpy as np


def select_is_query_in_posting_list(query, posting_list):
    for term in query.split():
        if term not in posting_list: return False
    return True


def select_list_intersection(list_1, list_2):
    return np.intersect1d(list_1, list_2)


def select_docs_from_AND_query(query, posting_list):
    query_tokens = query.split()

    for term in query_tokens:
        if term not in posting_list: return []

    query_matching_documents = posting_list[query_tokens.pop()]
    for term in query_tokens:
        if term not in posting_list: return []
        term_matching_documents = posting_list[term]
        query_matching_documents = select_list_intersection(term_matching_documents,
                                                            query_matching_documents)
    return sorted(query_matching_documents)


def select_docs_from_OR_query(query, posting_list):
    query_tokens = query.split()
    query_matching_documents = []
    for term in query_tokens:
        if term not in posting_list: continue
        query_matching_documents += posting_list[term]
        query_matching_documents = list(set(query_matching_documents))
    return sorted(query_matching_documents)
