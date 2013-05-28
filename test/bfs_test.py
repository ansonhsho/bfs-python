"""
Breadth First Search
@link https://github.com/adlawson/bfs-python
@author Andrew Lawson (http://adlawson.com)
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
import bfs

graph = {
    1:  {},
    2:  {},
    3:  {},
    4:  {},
    5:  {},
    6:  {},
    7:  {},
    8:  {},
    9:  {},
    10: {},
    11: {},
    12: {}
}

for edge in [[1,2], [1,3], [1,4], [2,5], [2,6], [4,7], [4,8], [5,9], [5,10], [7,11], [7,12]]:
    graph[edge[0]][edge[1]] = graph[edge[1]]
    graph[edge[1]][edge[0]] = graph[edge[0]]

visited = []
bfs.visit(1, graph, (lambda n: visited.append(str(n))))

print ', '.join(visited)
