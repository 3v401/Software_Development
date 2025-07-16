from itertools import zip_longest

def merge_strings_alternately(word1: str, word2: str) -> str:
    merged = []
    for c1, c2 in zip_longest(word1, word2, fillvalue=''):
        merged.append(c1)
        merged.append(c2)
    return ''.join(merged)


"""
Not optimized version:

def merge_strings_alternately(word1, word2):
    maxlen= max(len(word1), len(word2))
    outcome = ""
    for i in range(maxlen):
        if i < len(word1):
            outcome += word1[i]
        if i < len(word2):
            outcome += word2[i]
    return outcome
"""

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    result = merge_strings_alternately(word1, word2)
    print(result)