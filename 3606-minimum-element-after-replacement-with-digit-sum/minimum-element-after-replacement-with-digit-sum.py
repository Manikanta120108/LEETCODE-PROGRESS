class Solution:
    def minElement(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            digitsum = 0
            while i > 0:
                digitsum += i%10
                i //= 10
            l.append(digitsum)
        return min(l)