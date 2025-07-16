# URL: https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:

  my_dict = defaultdict(list)
  for word in strs:
    keys = ''.join(sorted(word))
    my_dict[keys].append(word)

  return list(my_dict.values())

if __name__ == '__main__':
  print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
  print(group_anagrams([""]))
  print(group_anagrams(["a"]))