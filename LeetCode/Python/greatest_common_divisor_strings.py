import math

def gcds(str1: str, str2: str) -> str:

  if str1 + str2 != str2+str1:
    return "" # Not divisible
  gcd=math.gcd(len(str1), len(str2))
  print(gcd)
  return str1[:gcd]

if __name__ == "__main__":
  print(gcds("ABCABC", "ABC"))
  print(gcds("ABABAB", "ABAB"))
  print(gcds("LEET", "CODE"))