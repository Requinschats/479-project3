import naive_indexer as ni
import SPIMI_indexer as si
from BM25.BM25 import BM25, select_reuters_fitted_BM25

# Subproject I:
# ni.select_global_posting_list(entry_limit=10000)
# si.select_global_posting_list(entry_limit=10000)
# SPIMI_posting_list = si.select_global_posting_list()

# Subproject II:
search_engine = select_reuters_fitted_BM25()
