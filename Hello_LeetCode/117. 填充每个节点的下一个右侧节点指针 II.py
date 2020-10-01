from Leetcode_type import *


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        tmp = []

        while queue:
            now_node = queue.pop(0)

            if queue:
                now_node.next = queue[0]
            else:
                now_node.next = None

            if now_node.left:
                tmp.append(now_node.left)
            if now_node.right:
                tmp.append(now_node.right)

            if not queue:
                queue = tmp
                tmp = []

        return root