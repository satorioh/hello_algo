class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


res = []


def pre_order(root):
    """前序遍历：根->左->右"""
    if root is None:
        return
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    """中序遍历：左->根->右"""
    if root is None:
        return
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)


def post_order(root):
    """后序遍历：左->右->根"""
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    res.append(root.val)
