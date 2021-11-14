import naive_indexer as ni
import SPIMI_indexer as si
from BM25.BM25 import select_reuters_fitted_BM25
from Boolean_Search_Engine.BSE import BSE

# Subproject I:
naive_indexer_limited_posting_list = ni.select_global_posting_list(entry_limit=10000)
SPIMI_indexer_limited_posting_list = si.select_global_posting_list(entry_limit=10000)

# final inverted index is created in BSE()
boolean_search_engine = BSE()
print(boolean_search_engine.search("pineapple"))
print(boolean_search_engine.search("pineapple Under", conjonction="AND"))
print(boolean_search_engine.search("pineapple Under", conjonction="OR"))

# Subproject II:
search_engine = select_reuters_fitted_BM25()
print("Result Format: Score, Doc ID")
print(search_engine.search("Democrats’ welfare and healthcare reform policies"))
print(search_engine.search("Drug company bankruptcies"))
print(search_engine.search("George Bush"))
