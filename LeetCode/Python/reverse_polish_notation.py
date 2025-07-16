# URL:
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

def erpn(tokens: list[str]) -> int:

  stack = []
  result = 0
  for token in tokens:

    if token in {"+", "-", "*", "/"}:

      b = stack.pop()
      a = stack.pop()

      if token == "+":
        result = a+b
      if token == "-":
        result = a-b
      if token == "*":
        result = a*b
      if token == "/":
        result == a//b

      stack.append(result)

    else:

      stack.append(int(token))

  return stack[0]

if __name__ == "__main__":
  print(erpn(["2","1","+","3","*"]))
  print(erpn(["4","13","5","/","+"]))