class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indes=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[indes]= nums[i]
                indes+=1
        return indes
    

    """ loog through to find a target value and remove all occurances
    populate the nums .. if value not val.. 
    """