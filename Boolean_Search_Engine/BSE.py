from Boolean_Search_Engine.selectors import select_is_query_in_posting_list, \
    select_docs_from_AND_query, select_docs_from_OR_query
from SPIMI_indexer import select_global_posting_list


class BSE:
    def __init__(self):
        self.posting_list = select_global_posting_list()

    def search(self, query, conjonction="AND"):
        if conjonction == "AND":
            return select_docs_from_AND_query(query, self.posting_list)
        if conjonction == "OR":
            return select_docs_from_OR_query(query, self.posting_list)
