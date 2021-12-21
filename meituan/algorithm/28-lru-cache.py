# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/21 1:46 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
运用你所掌握的数据结构，设计和实现一个LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶：你是否可以在O(1) 时间复杂度内完成这两种操作？
"""

"""我们可以总结出 cache 这个数据结构必要的条件：查找快，插入快，删除快，有顺序之分。"""

# 双链表，哈希链表（双向链表和哈希表的结合体）

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到头部(变成最新访问的)，所以定义一个方法
    def move_node_to_header(self, key):
        # 先将哈希表key指向的节点拎出来，为了简洁起名node
        #      hashmap[key]                               hashmap[key]
        #           |                                          |
        #           V              -->                         V
        # prev <-> node <-> next         pre <-> next   ...   node
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 之后将node插入到头部节点前
        #                   hashmap[key]                     hashmap[key]
        #                       |                                 |
        #                       V        -->                      V
        # header <-> next  ... node                   header <-> node <-> next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def add_node_to_header(self, key, value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new

    def pop_tail(self):
        last_node = self.tail.prev
        # 去掉链表尾部的节点在哈希表的对应项
        self.hashmap.pop(last_node.key)
        # 去掉最久没有被访问过的节点，即尾部Tail之前的一个节点
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        return last_node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到头部（变成最新访问的）
            self.move_node_to_header(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到链表头部
            self.move_node_to_header(key)
        else:
            if len(self.hashmap) >= self.capacity:
                # 若cache容量已满，删除cache中最不常用的节点
                self.pop_tail()
            self.add_node_to_header(key, value)


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    lru = LRUCache(2)
    print(lru.put(1, 1) == None)
    lru.put(2, 2)
    print(lru.get(1) == 1)
    lru.put(3, 3)
    print(lru.get(2) == -1)
    lru.put(4, 4)
    print(lru.get(1) == -1)
    print(lru.get(3) == 3)
    print(lru.get(4) == 4)
