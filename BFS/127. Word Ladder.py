#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/1 20:36
# @Author  : Jing
# @FileName: 127. Word Ladder.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/word-ladder/


class Solution:
    def ladderLength0(self, beginWord, endWord, wordList):
        queue = [(beginWord, 1)]
        visited = set()
        wordList = set(wordList)
        ls = set(beginWord+endWord+''.join(wordList))
        while queue:
            word, step = queue.pop(0)
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in ls:
                    if j != word[i]:
                        new_word = word[:i]+j+word[i+1:]
                        if new_word not in visited and new_word in wordList:
                            queue.append((new_word, step+1))
                            visited.add(new_word)
        return 0

    def ladderLength1(self, beginWord, endWord, wordList):
        import collections
        from collections import defaultdict
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

            # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

            # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


if __name__ == '__main__':
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(set(beginWord+endWord+''.join(wordList)))
    p = s.ladderLength2(beginWord, endWord, wordList)
    print(p)



