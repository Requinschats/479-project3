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
    print("DATE: " + str(select_query_doc_ids("DATE")))


def test_DANISH_is_valid_documents():
    print("Query test 2...")
    print("DANISH: " + str(select_query_doc_ids("DANISH")))


def test_THIS_IS_NOT_A_WORD_is_in_no_document():
    print("Query test 3...")
    print("Not a word: " + str(select_query_doc_ids("not a word")))


def challenge_query_1():
    print("Challenge query 1...")
    print("pineapple: " + str(select_query_doc_ids("pineapple")))


def challenge_query_2():
    print("Challenge query 2...")
    print("Phillippines: " + str(select_query_doc_ids("Phillippines")))


def challenge_query_3():
    print("Challenge query 3...")
    print("Brierley: " + str(select_query_doc_ids("Brierley")))


def challenge_query_4():
    print("Challenge query 4...")
    print("Chrysler: " + str(select_query_doc_ids("Chrysler")))


# challenge queries
challenge_query_1()
challenge_query_2()
challenge_query_3()
challenge_query_4()

# my initial tests
test_DATE_is_every_document()
test_DANISH_is_valid_documents()
test_THIS_IS_NOT_A_WORD_is_in_no_document()
