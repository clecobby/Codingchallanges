class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset= set(nums)
        longest = 0
        for num in numsset:
            if(num-1) not in numsset:
                length=1
                while(num+length)in numsset:
                    length +=1
                longest= max(length,longest)
        return longest