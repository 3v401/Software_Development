# URL: https://leetcode.com/problems/decode-ways/description/
# Dynamic programming:
"""
"count the number of ways" problem with dependent sub-results →
strong indicators for dynamic programming

The total ways to decode a string up to index i depends
on the solutions to previous subproblems (i-1, i-2).
"""
def decodeways(s: str) -> int:

  if not s or s[0]=="0":
    # edge case
    return 0

  n = len(s)
  dp = [0]*(n+1)
  # indexes [0,n] -> (n+1) elements
  dp[0]= 1
  # there is only one way to decode an empty string
  dp[1] = 1
  # there is only one way to decode a mono-string

  for i in range(2, n+1):
    # we already did i = 0,1
    if s[i-1]!="0":
      # if the element is not a 0, it can be decoded, 0 is string
      # index i is for dp[i], but we are analyzing s[i-1] for correct index handling
      dp[i]+=dp[i-1]

    two_digits=int(s[i-2:i])
    # two_digits convert to integer, correct handled as index is up to (but not included) i
    if 10<= two_digits <=26:
      dp[i]+=dp[i-2]

  return dp[n]

if __name__ == "__main__":
  print(decodeways("12"))
  print(decodeways("226"))
  print(decodeways("06"))