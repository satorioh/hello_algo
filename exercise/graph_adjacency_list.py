class Vertex:
    """顶点类"""

    def __init__(self, val: int):
        self.val = val


class GraphAdjList:
    """
    基于邻接表实现的无向图类
    顶点使用dict存储，边用list存储
    """

    def __init__(self, edges: list[list[Vertex]]):
        self.adj_dict = dict[Vertex, list[Vertex]]()
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self):
        return len(self.adj_dict)

    def add_vertex(self, vet: Vertex):
        if vet in self.adj_dict:
            return
        self.adj_dict[vet] = []

    def remove_vertex(self, vet: Vertex):
        if vet not in self.adj_dict:
            raise ValueError
        self.adj_dict.pop(vet)
        for key in self.adj_dict:
            edge_list = self.adj_dict[key]
            if vet in edge_list:
                edge_list.remove(vet)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_dict or vet2 not in self.adj_dict or vet1 == vet2:
            raise ValueError()
        self.adj_dict[vet1].append(vet2)
        self.adj_dict[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_dict or vet2 not in self.adj_dict or vet1 == vet2:
            raise ValueError()
        self.adj_dict[vet1].remove(vet2)
        self.adj_dict[vet2].remove(vet1)

    def print(self):
        """打印邻接表"""
        print("邻接表 =")
        for vertex in self.adj_dict:
            tmp = [v.val for v in self.adj_dict[vertex]]
            print(f"{vertex.val}: {tmp},")
