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


def sorted_tuples_by_second(tuples_list):
    return list(reversed(sorted(tuples_list, key=lambda tup: tup[1])))


def select_query_matching_documents_with_keyword_count(query_matching_documents):
    doc_id_keyword_count = {}
    for doc_id in query_matching_documents:
        if doc_id in doc_id_keyword_count:
            doc_id_keyword_count[doc_id] += 1
        else:
            doc_id_keyword_count[doc_id] = 0
    return doc_id_keyword_count.items()


def select_docs_from_OR_query(query, posting_list):
    query_tokens = query.split()
    query_matching_documents = []
    for term in query_tokens:
        if term not in posting_list: continue
        query_matching_documents += posting_list[term]
    return sorted_tuples_by_second(
        select_query_matching_documents_with_keyword_count(query_matching_documents))
