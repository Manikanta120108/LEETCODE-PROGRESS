class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1 = 0
        c2 = 0
        k = len(s)//2
        for i in range(k):
            if s[i] in "aeiouAEIOU":
                c1 += 1
            if s[k+i] in "aeiouAEIOU":
                c2 += 1
        return c1 == c2