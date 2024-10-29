class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        if nums[-1] < target:
            return ln
        if nums[0] > target:
            return 0
        for i in range(ln):
            if nums[i] >= target:
                return i
            
            
        