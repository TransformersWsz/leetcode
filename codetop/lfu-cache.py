'''
@File  : lfu-cache.py
@Author: Swift
@Date  : 2021/5/4 17:58
@Link  : https://leetcode-cn.com/problems/lfu-cache/
@Desc  : 460. LFU 缓存
@Method: 
'''

import collections


class Node:
    def __init__(self, key, val, freq=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.pre = pre
        self.next = next

    def insert(self, node):
        node.next = self.next
        node.next.pre = node
        self.next = node
        node.pre = self


def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.next = tail
    tail.pre = head
    return (head, tail)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.keyMap = {}
        self.freqMap = collections.defaultdict(create_linked_list)

    def delete(self, node):
        if node.pre:
            former = node.pre
            latter = node.next
            former.next = latter
            latter.pre = former

    def increase(self, node):
        self.delete(node)
        node.freq += 1
        self.freqMap[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        else:
            if self.minFreq == node.freq - 1:
                head, tail = self.freqMap[node.freq - 1]
                if head.next == tail:
                    self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            node = self.keyMap[key]
            self.increase(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key not in self.keyMap:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
                if self.size > self.capacity:
                    tod = self.freqMap[self.minFreq][0].next
                    self.delete(tod)
                    self.keyMap.pop(tod.key)
                    self.size -= 1
            else:
                node = self.keyMap[key]
                node.val = value
            self.increase(node)
