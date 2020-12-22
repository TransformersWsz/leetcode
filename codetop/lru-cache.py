'''
@File  : lru-cache.py
@Author: Swift
@Date  : 2020/12/22 12:13
@Link  : https://leetcode-cn.com/problems/lru-cache/
@Desc  : 146. LRU 缓存机制
@Method: https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
'''


class DLNode:
    def __init__(self, key, val, pre=None, nex=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nex = nex


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = DLNode(0, 0)
        self.tail = DLNode(0, 0)
        self.head.nex = self.tail
        self.tail.pre = self.head

    def add_node_to_head(self, node):
        tmp_next = self.head.nex
        self.head.nex = node
        node.pre = self.head
        node.nex = tmp_next
        tmp_next.pre = node

    def remove_node(self, node):
        pre_node = node.pre
        nex_node = node.nex
        pre_node.nex = nex_node
        nex_node.pre = pre_node

    def move_node_to_head(self, node):
        self.remove_node(node)
        self.add_node_to_head(node)

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.move_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.move_node_to_head(node)
        else:
            node = DLNode(key, value)
            self.d[key] = node
            self.add_node_to_head(node)
            if len(self.d) > self.capacity:
                last_node = self.tail.pre
                self.d.pop(last_node.key)
                self.remove_node(last_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)