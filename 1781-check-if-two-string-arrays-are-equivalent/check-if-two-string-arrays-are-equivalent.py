class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k1 = ''
        k2 = ''
        for i in word1:
            k1 += i
        for i in word2:
            k2 += i
        return k1 == k2
