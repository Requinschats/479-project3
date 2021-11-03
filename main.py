import naive_indexer as ni
import SPIMI_indexer as si

# Subproject I:
ni.select_global_posting_list(entry_limit=10000)
si.select_global_posting_list(entry_limit=10000)
SPIMI_posting_list = si.select_global_posting_list()
