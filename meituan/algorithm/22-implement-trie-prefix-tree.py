# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/19 10:13 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
"""

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


# 字典实现
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search_prefix(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.search_prefix(word)
        return node is not None and node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search_prefix(prefix) is not None


if __name__ == '__main__':
    s = Trie()
    s.insert('apple')
    print(s.search('apple'))
    assert s.search('apple') == True
    print(s.search('app'))
    assert s.search('app') == False
    print(s.startsWith('app'))
    assert s.startsWith('app') == True
    print(s.insert('app'))
    assert s.insert('app') == None
    print(s.search('app'))
    assert s.search('app') == True
