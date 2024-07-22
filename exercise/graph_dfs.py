from graph_adjacency_list import Vertex, GraphAdjList


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    """深度优先遍历辅助函数"""
    res.append(vet)
    visited.add(vet)
    vet_list = graph.adj_dict[vet]
    for v in vet_list:
        if v in visited:
            continue
        dfs(graph, visited, res, v)


def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """深度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    res = []
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res
