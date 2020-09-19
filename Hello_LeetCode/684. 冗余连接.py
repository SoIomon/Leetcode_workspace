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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)
        res = None
        for edge in edges:
            if uf.find_root(edge[0]) != uf.find_root(edge[1]):
                uf.union(edge[0], edge[1])
            else:
                res = edge
        return res