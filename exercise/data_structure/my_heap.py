class MyMaxHeap:
    """使用数组实现大顶堆"""

    def __init__(self):
        self.max_heap = []

    def size(self):
        return len(self.max_heap)

    def is_empty(self):
        return not self.max_heap

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def peek(self):
        return self.max_heap[0]

    def swap(self, i, j):
        """交换堆中的两个元素"""
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def push(self, val):
        self.max_heap.append(val)
        self.sift_up(self.size() - 1)

    def sift_up(self, i):
        """从节点 i 开始，从底至顶堆化"""
        while True:
            p_index = self.parent(i)
            # 当“越过根节点”或“节点无须修复”时，结束堆化
            if p_index < 0 or self.max_heap[i] <= self.max_heap[p_index]:
                break
            # 交换两节点
            self.swap(i, p_index)
            # 循环向上堆化
            i = p_index

    def pop(self):
        if self.is_empty():
            raise IndexError("堆为空")
        # 交换根节点和最后一个节点
        self.swap(0, self.size() - 1)
        # 删除最后一个节点
        val = self.max_heap.pop()
        # 从顶至下进行堆化
        self.sift_down(0)
        return val

    def sift_down(self, i: int):
        """从节点 i 开始，从顶至底堆化"""
        while True:
            # 判断节点 i, l, r 中值最大的节点，记为 ma
            l_index, r_index, max_index = self.left(i), self.right(i), i
            if l_index < self.size() and self.max_heap[l_index] > self.max_heap[max_index]:
                max_index = l_index
            if r_index < self.size() and self.max_heap[r_index] > self.max_heap[max_index]:
                max_index = r_index
            # 若节点 i 最大或索引 l, r 越界，则无须继续堆化，跳出
            if max_index == i:
                break
            # 交换两节点
            self.swap(i, max_index)
            # 循环向下堆化
            i = max_index
