class Solution:
            
                
        
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        my_map = {}
        
        for index, num in enumerate(nums):
            if num not in my_map:
                my_map[num] = index
        i = 0
        for key in my_map:
            nums[i] = key
            i+=1
        
        return len(my_map)
                
                
            