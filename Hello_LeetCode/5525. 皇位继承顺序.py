from Leetcode_type import *

class Node:
    def __init__(self, name: str):
        self.name = name
        self.children: List[Node] = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.death_set = set()
        self.jiapu = Node(kingName)
        self.p_map = {kingName: self.jiapu}

    def birth(self, parentName: str, childName: str) -> None:
        tmp = Node(childName)
        self.p_map[parentName].children.append(tmp)
        self.p_map[childName] = tmp

    def death(self, name: str) -> None:
        self.death_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        stack = [self.jiapu]

        while stack:
            now_node = stack.pop(-1)
            if now_node.name not in self.death_set:
                ans.append(now_node.name)
            for child in now_node.children[::-1]:
                stack.append(child)
        return ans



obj = ThroneInheritance('king')
obj.birth('king', 'andy')
obj.birth('king', 'bob')
print(obj.getInheritanceOrder())