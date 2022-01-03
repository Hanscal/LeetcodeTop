# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 10:42 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""

class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int: # remove
        while len(self.stack) != 1:
            self.stack2.append(self.stack.pop())
        r = self.stack.pop()
        while self.stack2:
            self.stack.append(self.stack2.pop())
        return r

    def peek(self) -> int: # return
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_3 = obj.peek()
    param_2 = obj.pop()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)
    assert param_2 == 1
    assert param_3 == 1
    assert param_4 == False