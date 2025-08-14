class Solution:
    def hasDuplicate(self,nums:list[int])-> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
    
    
    
if __name__=="__main__":
    solution = Solution()
    nums= [2,34,5,3,]
    results=solution.hasDuplicate(nums)
    print(results)