# URL: https://leetcode.com/problems/decode-ways/description/
# Dynamic programming:

def decodeways(s: str) -> int:

  if not s or s[0]=="0":
    return 0

  n = len(s)
  dp = [0]*(n+1)
  dp[0]= 1
  dp[1] = 1

  for i in range(2, n+1):
    if s[i-1]!="0":
      dp[i]+=dp[i-1]

    two_digits=int(s[i-2:i])
    if 10<= two_digits <=26:
      dp[i]+=dp[i-2]

  return dp[n]

if __name__ == "__main__":
  print(decodeways("12"))
  print(decodeways("226"))
  print(decodeways("06"))