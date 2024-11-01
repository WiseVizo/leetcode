class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_map = {}
        for ele in nums:
            if ele in my_map:
                my_map[ele] = my_map[ele] + 1
                continue
            my_map[ele] = 1
        
        for key , value in my_map.items():
            if value == 1:
                return key
        