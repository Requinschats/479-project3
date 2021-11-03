class PostingList:
    def __init__(self, entry_limit=None):
        self.values = {}
        self.entry_count = 0
        self.entry_limit = entry_limit

    def add_term_doc_id(self, term_doc_id):
        term, doc_id = term_doc_id
        if term in self.values:
            self.values[term].append(doc_id)
        else:
            self.values[term] = [doc_id]
            self.entry_count += 1

    def add_token_array_to_posting(self, token_array, doc_id):
        list(map(lambda token: self.add_term_doc_id((token, doc_id)), token_array))

    def has_reached_subproject1_maximum_entries(self):
        return self.entry_count >= self.entry_limit if self.entry_limit is not None else False
