# URL: https://leetcode.com/problems/word-ladder-ii/description/

from collections import defaultdict
class Solution:
    def word_ladder_ii(self, beginWord: str, endWord: str, wordList: list[list[str]]) -> list[str]:

        wordset = set(wordList)
        # O(1) Access time
        if endWord not in wordset:
            # edge case
            return []
        
        layer = {beginWord: [[beginWord]]}
        # The easiest path is beginWord -> beginWord
        while layer:
            # while the layer is not empty
            new_layer = defaultdict(list)
            # create a new one to store the new paths to endWord
            for word in layer:
                # For each key
                if word == endWord:
                    # if the key is the endWord, return the paths
                    return layer[word]
                
                for i in range(len(word)):
                    # change each character in word
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        # for each letter in the alphabet
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in wordset:
                            # we found a word
                            for path in layer[word]:
                                new_layer[new_word].append(path + [new_word])
                            # we use append because it is defaultdict(list)
            wordset -= set(new_layer.keys())
            # delete the words from the wordset to avoid infinite loops
            layer = new_layer
            # update layer content. If no words found, layer will be empty

        # if finished the while and not solution found, return empty list
        return []

if __name__ == '__main__':

    sol = Solution()
    print(sol.word_ladder_ii('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))