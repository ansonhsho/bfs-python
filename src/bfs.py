"""
Breadth First Search
@link https://github.com/adlawson/bfs-python
@author Andrew Lawson (http://adlawson.com)
"""

"""
:param {List} frontier
:param {Dict} graph
:param {Lambda} fn
"""
def _visit(frontier, graph, fn):
    level = 0
    levels = {}

    while 0 < len(frontier):
        next = []
        for node in frontier:
            fn(node)
            levels[node] = level
            for adj, tree in sorted(graph[node].items()):
                if adj not in levels:
                    next.append(adj)
        frontier = next
        level += 1

"""
:param {Integer} node
:param {Dict} graph
:param {Lambda} fn
"""
def visit(node, graph, fn):
    _visit([node], graph, fn)
