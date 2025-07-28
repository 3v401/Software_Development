# URL: https://leetcode.com/problems/word-break/description/

def wordbreak(s: str, wordDict: list[str]) -> bool:

  wordset = set(wordDict)
  n = len(s)
  dp = [False]*(n+1)
  dp[0] = True

  for i in range(1, n+1):
    for j in range(i):
      if dp[j] and (s[j:i] in wordset):
        dp[i] = True
        break

  return dp[n]

if __name__ == '__main__':
  print(wordbreak("leetcode", ["leet","code"]))
  print(wordbreak("applepenapple", ["apple","pen"]))
  print(wordbreak("catsandog", ["cats","dog","sand","and","cat"]))