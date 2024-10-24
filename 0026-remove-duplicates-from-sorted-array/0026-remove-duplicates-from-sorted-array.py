class Solution:
            
                
        
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        i = 0
        while len(nums)-1>i:
            if nums[i] == nums[i+1]:
                del nums[i+1]
                continue
            i+=1
        return len(nums)
                
                
            