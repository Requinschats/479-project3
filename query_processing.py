from naive_indexer import select_global_posting_list


def select_query_doc_ids(string):
    posting_list = select_global_posting_list()
    if string in posting_list:
        return posting_list[string]
    else:
        return []


# tests made from run on first 5 docs

def test_DATE_is_every_document():
    print("Query test 1...")
    selected = select_query_doc_ids("DATE")
    assert selected == ['4001', '10001', '11001', '5001', '13001']


def test_DANISH_is_valid_documents():
    print("Query test 2...")
    selected = select_query_doc_ids("DANISH")
    assert selected == ['4001', '10001', '11001', '5001']


def test_THIS_IS_NOT_A_WORD_is_in_no_document():
    print("Query test 3...")
    selected = select_query_doc_ids("THIS_IS_NOT_A_WORD")
    assert selected == []


test_DATE_is_every_document()
test_DANISH_is_valid_documents()
test_THIS_IS_NOT_A_WORD_is_in_no_document()
