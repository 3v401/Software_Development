# URL: https://leetcode.com/problems/palindromic-substrings/description/

def palindromicsubstring(s: str) -> int:

    odd_palindromes, even_palindromes = 0, 0
    # number of palindromes
    for i in range(len(s)):

        odd_palindromes += count_palindromes(s, i, i)
        even_palindromes += count_palindromes(s, i, i+1)

    return odd_palindromes + even_palindromes

def count_palindromes(s: str, lpoint: int, rpoint: int) -> int:

    count = 0
    while lpoint >= 0 and rpoint<len(s) and s[lpoint]==s[rpoint]:
        
        # condition to be considered palindrome
        count+=1
        lpoint-=1
        rpoint+=1

    return count

if __name__ == "__main__":

    print(palindromicsubstring("abc"))
    print(palindromicsubstring("aaa"))