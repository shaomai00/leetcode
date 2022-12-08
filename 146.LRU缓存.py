from __future__ import annotations
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 一个哈希表存储关键字和node关系，一个头尾相接的双向链表控制快速删除和加入
from dataclasses import dataclass
@dataclass
class Node:
    key: int
    val: int
    next: Node = None
    pre: Node = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.dict = {}

    def addAfterHead(self,node: Node):
        # 新的不要直接插在头结点前面，要插在头结点后面，不然尾结点就连不上了
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node:Node):
        node.next.pre = node.pre
        node.pre.next = node.next

    def move2head(self, node:Node):
        self.removeNode(node)  # 先断开原来的
        self.addAfterHead(node) # 再连到头结点后边

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.move2head(node) # 刷到头结点后边
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.move2head(node) # 刷
        else:
            if len(self.dict) == self.capacity:
                node = self.tail.pre
                self.removeNode(node)  # 断开这个尾结点
                del self.dict[node.key]
            node = Node(key,value)
            self.addAfterHead(node) # 新的插头
        self.dict[key] = node

if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1))
    obj.put(3,3)
    print(obj.get(2))
    obj.put(4,4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
