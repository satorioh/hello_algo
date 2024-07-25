"""
基于数组表示的二叉树：
给定某节点，获取它的值、左（右）子节点、父节点。
获取前序遍历、中序遍历、后序遍历、层序遍历序列。
"""


class ArrayBinaryTree:
    """数组表示下的二叉树类"""

    def __init__(self, arr):
        self._tree = list(arr)

    def size(self):
        return len(self._tree)

    def val(self, i):
        """获取索引为 i 节点的值"""
        # 若索引越界，则返回 None ，代表空位
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        """获取索引为 i 节点的左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        """获取索引为 i 节点的右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        """获取索引为 i 节点的父节点的索引"""
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
