"""
File: binary_tree.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
"""

import sys, os.path as osp

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from include import *


""" Driver Code """
if __name__ == "__main__":
    # 初始化二叉树
    # 初始化节点
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print_tree(n1)

    # 插入与删除结点
    P = TreeNode(0)

    # 在 n1 -> n2 中间插入节点 P
    n1.left = P
    P.left = n2
    print_tree(n1)

    # 删除结点
    n1.left = n2
    print_tree(n1)
