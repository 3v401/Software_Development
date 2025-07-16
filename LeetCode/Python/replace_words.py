# URL: https://leetcode.com/problems/replace-words/description/

class NodeTrie:
  # Define a Node. Each has children and a flag to end
  def __init__(self):
    self.children = {}
    self.end_of_word = False

class Trie:
  # Define the Trie tree. Each tree has a Node root
  def __init__(self):
    self.root = NodeTrie()

  def insert(self, word:str):
    # The Trie tree also has the insert function that projects the root codification
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] =  NodeTrie()
      node = node.children[char]

    node.end_of_word = True

  def find_shortest_prefix(self, word: str) -> str:
    # The Trie tree also has the find shortest prefix to find it on each received word
    node = self.root
    prefix = ''

    for char in word:
      if char not in node.children:
        return word
      node = node.children[char]
      prefix += char

      if node.end_of_word:
        return prefix

    return word


def replace_words(dictionary: list[str], sentence:str) -> str:
  # Call the function replace_words that calls the class to substitute word -> root
  tree = Trie()
  for word in dictionary:
    tree.insert(word)

  words = sentence.split()
  outcome = [tree.find_shortest_prefix(word) for word in words]

  return ' '.join(outcome)


if __name__ == '__main__':
  print(replace_words(["cat","bat","rat"], "the cattle was rattled by the battery"))
  print(replace_words(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))