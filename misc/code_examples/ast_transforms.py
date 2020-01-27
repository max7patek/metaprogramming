

from ast import parse, unparse, dump, Import, ImportFrom, Module

from functools import partial

from collections import defaultdict

from copy import deepcopy

import debug_decorator


def sort_imports(node):
    imports = []
    import_froms = defaultdict(list)
    remainder = []
    for stmnt in node.body:
        if isinstance(stmnt, Import):
            imports.extend(stmnt.names)
        elif isinstance(stmnt, ImportFrom):
            import_froms[stmnt.module].extend(stmnt.names)
        else:
            remainder.append(stmnt)

    new_body = []
    for key in sorted(import_froms.keys()):
        aliases = sorted(import_froms[key], key=lambda i: i.name)
        new_body.append(ImportFrom(module=key, names=aliases, level=0))
    for alias in sorted(imports, key=lambda i: i.name):
        new_body.append(Import(names=[alias]))
    new_body.extend(remainder)

    out = deepcopy(node)
    out.body = new_body   
    return out

    

with open(__file__) as self:
    self_str = "".join(self)
    self_node = parse(self_str)
    sorted_self = sort_imports(self_node)
    print(dump(sorted_self, indent=2))
    print(unparse(sorted_self))

