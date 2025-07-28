# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lswrc(s:str) -> int:

    seen = set()
    # Access O(1)
    maxlen = 0
    lpoint = 0
    for rpoint in range(len(s)):
        char = s[rpoint]
        while char in seen:
            # if char in seen -> move lpoint+=1 until char is removed from seen
            seen.remove(s[lpoint])
            lpoint +=1

        seen.add(s[rpoint])
        # store new seen character
        maxlen = max(maxlen, rpoint-lpoint+1)
        # compute new maxlen

    return maxlen

if __name__ == "__main__":

    print(lswrc("abcabcbb"))
    print(lswrc("bbbbb"))
    print(lswrc("pwwkew"))