from Leetcode_type import *

class UnionFind:
    def __init__(self, node_num: int):
        self.node_list = list(range(node_num))

    def find_root(self, index: int):
        node = index
        while node != self.node_list[node]:
            node = self.node_list[node]
        return node

    def union(self, node_1: int, node_2: int):
        self.node_list[self.find_root(node_1)] = self.find_root(node_2)

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        node_count = len(edges) + 1
        uf = UnionFind(node_count)
        parent = list(range(node_count))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find_root(node1) == uf.find_root(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)
        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]


print(Solution().findRedundantDirectedConnection( [[1,2], [1,3], [2,3]]))