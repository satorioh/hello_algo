a = [7, 1, 2, 4, 6, 8, 3, 5, 9, 10]


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_bst(arr):
    if not arr:
        return None
    arr.sort()
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = build_bst(arr[:mid])
    root.right = build_bst(arr[mid + 1:])
    return root


root = build_bst(a)


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.val)
    inorder(root.right)


inorder(root)
