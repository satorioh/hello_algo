class GraphAdjMat:
    """基于邻接矩阵实现的无向图类"""

    def __init__(self, vertices: list[int], edges: list[list[int]]):
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应“顶点索引”
        self.adj_mat: list[list[int]] = []
        for val in vertices:
            self.add_vertex(val)
        for pair in edges:
            self.add_edge(pair[0], pair[1])

    def size(self):
        """获取顶点数量"""
        return len(self.vertices)

    def add_vertex(self, val):
        n = self.size()
        self.vertices.append(val)
        new_row = [0] * n
        # 添加行
        self.adj_mat.append(new_row)
        # 添加列
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index):
        if index > self.size():
            raise IndexError
        self.vertices.pop(index)
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i, j):
        # 索引越界与相等处理
        if i < 0 or j < 0 or i > self.size() or j > self.size() or i == j:
            raise IndexError
        # 在无向图中，邻接矩阵关于主对角线对称，即满足 (i, j) == (j, i)
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i, j):
        # 索引越界与相等处理
        if i < 0 or j < 0 or i > self.size() or j > self.size() or i == j:
            raise IndexError
        # 在无向图中，邻接矩阵关于主对角线对称，即满足 (i, j) == (j, i)
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        print(self.adj_mat)
