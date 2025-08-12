# URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

# We will use a Trie with adaptation for the dots

class WordDictionary:

    class Node:
        __slots__=('children', 'end')
        # __slots__ tells Python this class will only have 'children' and 'end' attributes.
        # This avoids creating a per-instance __dict__, saving memory when many Nodes exist.
        def __init__(self):
            self.children = {}
            self.end = False
            # children: Each node gets its own dict for child nodes (char -> Node)

    def __init__(self):
        self.root = WordDictionary.Node()
        # Root from we start

    def addWord(self, word: str) -> None:
        # No content returned
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary.Node()
                # Create a new node in children[char] if no node exists
            node = node.children[char]
            # move to that child
        node.end = True
        # End of the word reached

    def search(self, word: str) -> bool:
        # return boolean if word found
        # required dfs to solve '.' situation
        def dfs(index: int, node: 'WordDictionary.Node') -> bool:
            if index==len(word):
                # reached the end
                return node.end
            char = word[index]
            if char == '.':
                # If wildcard found
                for nxt in node.children.values():
                    # For first children in current node
                    # call dfs again
                    if dfs(index + 1, nxt):
                        # If the next dfs call returns True
                        return True
                return False
            else:
                nxt = node.children.get(char)
                if nxt is None:
                    # If this node doesn't have that char as children
                    return False
                # call dfs iteratively (next node)
                return dfs(index+1, nxt)
        
        # call dfs since root Node
        return dfs(0, self.root)
        
if __name__ == '__main__':

    sol = WordDictionary()
    sol.addWord('bad')
    sol.addWord('dad')
    sol.addWord('mad')
    print(sol.search('pad'))
    print(sol.search('bad'))
    print(sol.search('.ad'))
    print(sol.search('b..'))