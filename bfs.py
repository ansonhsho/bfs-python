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

def visit(node, graph, fn):
    _visit([node], graph, fn)
