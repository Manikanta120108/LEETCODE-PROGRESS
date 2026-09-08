class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l= []
        for i in nums:
            if nums.count(i) == 2:
                l.append(i)
        return list(set(l))