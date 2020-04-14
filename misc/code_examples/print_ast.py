

import ast
from collections import defaultdict
import pygraphviz as pgv

class AstGraphGenerator(object):

    def __init__(self):
        self.graph = defaultdict(lambda: [])
        self.uid = 0
        self.short_ids = {}

    def __str__(self):
        return str(self.graph)

    def _id(self, node):
        if isinstance(node, str) or isinstance(node, int):
            self.uid += 1
            return f"{node} ({self.uid})"
        if id(node) not in self.short_ids:
            self.uid += 1
            self.short_ids[id(node)] = self.uid
        return f"{node.__class__.__name__} ({self.short_ids[id(node)]})"

    def visit(self, node):
        """Visit a node."""
        for cls in node.__class__.__mro__:
            method = 'visit_' + cls.__name__
            #print(f"looking for {method}")
            visitor = getattr(self, method, None)
            if visitor:
                break
        else:
            visitor = self.generic_visit
            print(f"calling {visitor.__name__} for {node}, {type(node)}")
        return visitor(node)

    def visit_AST(self, node):
        for key, value in ast.iter_fields(node):
            if value is None:
                continue
            elif isinstance(value, list):
                list_id = self._id(key)
                self.graph[self._id(node)].append(list_id)
                for item in value:
                    self.graph[list_id].append(self._id(item))
                    self.visit(item)
            else:
                self.graph[self._id(node)].append(self._id(value))
                self.visit(value)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        return str(node)

code = """
def foo(a, b):
    if True:
        return
    c = sum(1, a - b)
"""
node = ast.parse(code)
print(code)
print(ast.dump(node))
visitor = AstGraphGenerator()
visitor.visit(node)
G = pgv.AGraph(visitor.graph)
G.graph_attr["bgcolor"] = "transparent"
G.layout(prog="dot")
G.draw('file.png')

