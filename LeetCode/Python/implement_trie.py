# URL: https://leetcode.com/problems/implement-trie-prefix-tree/description/

"""
Use __slots__ when:

1. You’ll create many instances of a class.
2. Each instance has a fixed set of attributes.
3. You want to reduce memory footprint and maybe gain a small speed boost.

Don’t __slots__ when:

1. You need to add attributes dynamically later.

"""

class Trie:
    class Node:
        # We define the Node class inside Trie class
        __slots__ = ('children', 'end')
        def __init__(self):
            self.children = {}
            self.end = False
        # By defect we have empty dict and False boolean

    def __init__(self):
        self.root = Trie.Node()
        # We create a root node to start from always

    def insert(self, word: str) -> None:
        
        node = self.root
        # move to the root
        for char in word:
            if char not in node.children:
                # if the character not in children, add it
                node.children[char] = Trie.Node()
            node = node.children[char]
            # move to this child
        node.end = True
        # When loop finishes, the word is ended

    def search(self, word: str) -> bool:

        node = self.root
        for char in word:
            if char not in node.children:
                return False
                # That word doesn't exist
            node = node.children[char]
            # move to that child

        return node.end
    
    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
        # Not required to check whether the word finishes, prefix is found

if __name__ == '__main__':

    sol = Trie()
    sol.insert('hi')
    print(sol.search('bye'))
    print(sol.search('hi'))
    print(sol.startsWith('h'))