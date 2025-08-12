# URL: https://leetcode.com/problems/word-break/description/

"""
applepenapple

[       a     ap     app    appl   apple, p     pe      pen,   a    ap      app     appl, apple]
[True, False, False, False, False, True, False, False, True, False, False, False, False, True]
"""


def wordbreak(s: str, wordDict: list[str]) -> bool:

  if not s:
      # edge case
      return False

  wordset = set(wordDict)
  # Access O(1)
  n = len(s)
  dp = [False]*(n+1)
  dp[0] = True
  # It is possible to segmentate empty string

  for i in range(1, n+1):
    # for each cell in dp (0 is already defined)
    for j in range(i):
      # for each char in s (from j to i)
      if dp[j] and (s[j:i] in wordset):
        # if previous subdivision is True, and the new one is in wordset
        dp[i] = True
        # This one is also True
        break
      # no need to keep searching in j since dp[i] is detected as True

  # final string is divided completely in last cell
  return dp[n]

if __name__ == '__main__':
  print(wordbreak("leetcode", ["leet","code"]))
  print(wordbreak("applepenapple", ["apple","pen"]))
  print(wordbreak("catsandog", ["cats","dog","sand","and","cat"]))