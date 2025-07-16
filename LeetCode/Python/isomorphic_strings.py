# URL:
# https://leetcode.com/problems/isomorphic-strings/description/

def isomorphic_strings(s: str, t: str) -> bool:

  if len(s) != len(t):
    return False

  s_dict = {}
  t_dict = {}

  for sc, tc in zip(s, t):

    if sc in s_dict:
      if s_dict[sc] != tc:
        return False
    else:
      s_dict[sc] = tc

    if tc in t_dict:
      if t_dict[tc] != sc:
        return False
    else:
      t_dict[tc] = sc

  return True

if __name__ == "__main__":
  print(isomorphic_strings("egg", "add"))
  print(isomorphic_strings("foo", "bar"))
  print(isomorphic_strings("paper", "title"))
  print(isomorphic_strings("ab", "aa"))