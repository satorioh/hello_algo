class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

# 插入：在 n1 -> n2 中间插入节点 P
p = TreeNode(val=6)
n1.left = p
p.left = n2

# 删除p
n1.left = n2
