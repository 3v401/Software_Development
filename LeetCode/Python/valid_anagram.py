# URL:
# https://leetcode.com/problems/valid-anagram/

from collections import Counter

def validanagram(s: str, t:str) -> bool:

  if len(s) != len(t):
    return False
  
  s_dict=Counter(s)
  t_dict=Counter(t)
  for char in s_dict:
    if s_dict[char] != t_dict[char]:
      return False
  
  return True


if __name__ == "__main__":
  print(validanagram("anagram", "nagaram"))
  print(validanagram("rat", "car"))