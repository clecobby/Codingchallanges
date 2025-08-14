class Solution():
    def hasDuplicate(self, nums:list[int])-> bool:
        for i in range (len(nums)):
            for ii in range (1+i,len(nums)):
                if nums[i]==nums[ii]:
                    return True
        return False
    
    
    
if __name__=="__main__":
    solution= Solution()
    nums=[1,3,5,3,4]
    results=solution.hasDuplicate(nums)
    print(results)