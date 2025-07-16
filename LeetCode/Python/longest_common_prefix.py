# URL: https://leetcode.com/problems/longest-common-prefix/description/

def lcp(strs: list[str]) -> str:

  if not strs:
    return ""

  strs.sort()
  # If there's a common prefix across all strings,
  # it must exist between the first and last after sorting — because all others lie between them.
  # So instead of comparing every pair of strings, we compare:
  first, last = strs[0], strs[-1]

  i = 0
  # Loop through both strings one character at a time:
  while i < len(first) and i< len(last) and first[i] == last[i]:
    i +=1

  return first[:i]


if __name__ == "__main__":
  print(lcp(["flower","flow","flight"]))
  print(lcp(["dog","racecar","car"]))
  print(lcp(["interview","internal","internet", "interval"]))
  """
  Sorting guarantees that the first and last strings will have the maximum possible difference,
  so the common prefix between them is the longest shared among all strings.
  """