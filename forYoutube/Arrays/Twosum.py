class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for i, v in enumerate (nums):
            diff = target - v
            if diff in remainder:
                return [remainder[diff],i]
            remainder[v]=i