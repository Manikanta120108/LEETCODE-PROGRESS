class Solution:
    def isThree(self, n: int) -> bool:
        fc = 0
        for i in range(1, n+1):
            if n%i == 0:
                fc += 1
        return fc == 3
        