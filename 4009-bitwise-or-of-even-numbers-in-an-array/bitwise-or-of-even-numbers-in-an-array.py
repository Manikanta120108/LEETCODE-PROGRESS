class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if i%2 == 0:
                k |= i
        return k