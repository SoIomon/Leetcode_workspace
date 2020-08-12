# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(root:Node):
            if not root:
                return None

            ret = Node(val=root.val)
            visited[root.val] = ret
            for neighbor in root.neighbors:
                if neighbor.val in visited:
                    ret.neighbors.append(visited[neighbor.val])
                else:
                    ret.neighbors.append(dfs(neighbor))
            return ret

        return dfs(node)

