from graph_adjacency_list import Vertex, GraphAdjList
from collections import deque


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """广度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []
    # 哈希集合，用于记录已被访问过的顶点
    visited = set[Vertex]([start_vet])
    que = deque[Vertex]([start_vet])
    # 以顶点 vet 为起点，循环直至访问完所有顶点
    while len(que) > 0:
        vet = que.popleft()
        res.append(vet)
        vet_list = graph.adj_dict[vet]
        for v in vet_list:
            if v in visited:
                continue
            visited.add(v)
            que.append(v)
    return res
