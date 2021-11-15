import BM25.selectors as s


def select_reuters_fitted_BM25(k1=1.5, b=0.75):
    print("Building BM25 reuters search engine...\n")
    tokenized_documents = s.select_tokenized_reuters21578_document_list()
    bm25 = BM25(k1, b)
    bm25.initialize(tokenized_documents)
    return bm25


class BM25:
    # from textbook
    # k1 calibrates the document term frequency scaling
    # b determines the scaling by document length
    def __init__(self, k1=1.60, b=0.9):
        self.b, self.k1 = b, k1

    def initialize_term_inverse_document_frequency(self, term, frequency):
        self.inverse_document_frequency[term] = s.select_inverse_document_frequency(
            self.corpus_size, frequency)

    def initialize_average_doc_length(self):
        self.average_doc_length = s.select_average_doc_length(self.total_doc_length,
                                                              self.corpus_size)

    def initialize(self, corpus):
        self.corpus = corpus
        self.inverse_document_frequency = {}
        self.corpus_size, self.total_doc_length, frequencies, self.term_frequency, self.document_frequency = s.select_BM25_initial_values_from_corpus(
            corpus)

        for term, frequency in self.document_frequency.items():
            self.initialize_term_inverse_document_frequency(term, frequency)

        self.initialize_average_doc_length()
        return self

    def search(self, query):
        return s.select_query_scores(self.get_query_score, query, self.corpus)

    def select_term_doc_query_score(self, term, frequency, doc_index):
        return (s.select_BM25_numerator(self, term, frequency) / s.select_BM25_denominator(self,
                                                                                           frequency,
                                                                                           doc_index))

    def get_query_score(self, query, doc_index, doc_id):
        doc_query_score = 0.0
        doc_term_frequencies = self.term_frequency[doc_index]
        for term in query:
            if term not in doc_term_frequencies: continue
            frequency = doc_term_frequencies[term]
            doc_query_score += self.select_term_doc_query_score(term, frequency, doc_index)
        return doc_query_score, doc_id
