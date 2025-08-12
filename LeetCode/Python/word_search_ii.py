# URL: https://leetcode.com/problems/word-search-ii/description/

"""
We will use a DFS modified that follows the guidance of a previously defined Trie
"""

class NodeTrie:
    
	__slots__ = ('children', 'word')
	def __init__(self):
		self.children: dict[str, NodeTrie] = {}
		self.word: str | None = None
		# Most optimal way to define parameters for storage (__slots__) and devs : dict[] = {}

class Solution:

	def findWord(self, board: list[list[str]], words: list[str]) -> list[str]:

		# Define Trie + run DFS -> outcome: list of words found in the grid
		# Define Trie: ---------
		root = NodeTrie()

		for word in words:
			node = root
			# reset position
			for char in word:
				if char not in node.children:
					# If char doesn't exist in the Trie, create node and add char
					node.children[char] = NodeTrie()
				node = node.children[char]
				# move to the children node
			node.word = word
			# When arrived to the end of the word (Trie branch) and word label to know it finished the word

		# ----------------------

		# Parameters to run dfs
		rows, cols = len(board), len(board[0])
		res: list[str] = []
		# res: answer to the program, contains word, better defined for devs (readability)

		# Define DFS: ----------
		def dfs(r: int, c: int, node: NodeTrie):
			# Doesn't return content, only appends words to res
			char = board[r][c]

			if char not in node.children:
				# There is no word that starts/continues with that character in Trie branch
				return
			
			# If it exists, move to the next character
			nxt = node.children[char]

			if nxt.word is not None:
				# If a word exists at this Trie step
				res.append(nxt.word)
				nxt.word = None
				# Add word to res and delete label to avoid duplicates

			board[r][c] = '#'
			# Mark current cell as visited

			if r>0: dfs(r-1, c, nxt)				# up
			if r+1<rows: dfs(r+1, c, nxt)			# down
			if c>0: dfs(r, c-1, nxt)				# left
			if c+1<cols: dfs(r, c+1, nxt)			# right
			# call recursively while inside the board constraints

			board[r][c] = char
			# set back its true value

			if not nxt.children:
				# after iterating throughout all the Trie, there is no purpose in saving that path
				# delete it
				node.children.pop(char)

		for r in range(rows):
			for c in range(cols):
				dfs(r, c, root)
				# do dfs guided by the Trie starting from the root.
				# Iteratively inside will call the rest of letters

		return res 


if __name__ == '__main__':
	
	sol = Solution()
	print(sol.findWord([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
	print(sol.findWord([["a","b"],["c","d"]], ["abcb"]))