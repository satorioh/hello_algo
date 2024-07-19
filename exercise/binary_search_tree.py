class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, num):
    cur = root
    while cur:
        if cur.val < num:
            cur = cur.right
        elif cur.val > num:
            cur = cur.left
        else:
            return cur


def insert(root, num):
    """插入节点"""
    # 若树为空，则初始化为根节点
    if root is None:
        root = TreeNode(num)
        return

    cur, pre = root, None
    while cur is not None:
        # 找到重复节点，直接返回
        if cur.val == num:
            return
        pre = cur
        if cur.val < num:
            cur = cur.right
        else:
            cur = cur.left
    # 插入节点
    node = TreeNode(num)
    if pre.val < num:
        pre.right = node
    else:
        pre.left = node
