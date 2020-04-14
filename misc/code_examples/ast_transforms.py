
import sys
from ast import parse, unparse, dump, Import, ImportFrom, Module, fix_missing_locations
from functools import partial
from collections import defaultdict
from copy import deepcopy
import debug_decorator




def sort_imports(node):
    """sorts the node in place"""
    imports = [stmnt for stmnt in node.body 
              if isinstance(stmnt, Import)]
    imports = [name for imp in imports for name in imp.names]
    import_froms = [stmnt for stmnt in node.body 
                   if isinstance(stmnt, ImportFrom)]
    remainder = [stmnt for stmnt in node.body 
                if not (stmnt in imports or stmnt in import_froms)]
    imports.sort(key=lambda i: i.name)
    import_froms.sort(key=lambda i: i.module)
    for impfrm in import_froms:
        impfrm.names.sort(key=lambda i: i.name)
    # print([alias.name for alias in import_froms[-1].names])
    node.body = import_froms + imports + remainder
    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        filename = __file__
    else:
        filename = sys.argv[1]
    with open(filename) as self:
        self_str = "".join(self)
        node = parse(self_str)
        sort_imports(node)
        print(unparse(node))

