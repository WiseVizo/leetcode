class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []
        ln = len(nums)
        if ln<=0:
            return r
        lower = nums[0]
        upper = lower
        for i in range(1, len(nums)):
            if nums[i-1]!= nums[i] - 1:
                upper = nums[i-1]
                self.generateRange(lower, upper, r)
                # reset upper and lower
                lower = nums[i]
                upper = lower
                continue
            if nums[i-1] == nums[i] - 1:
                upper = nums[i]
        self.generateRange(lower, upper, r)
        return r
    
    def generateRange(self, lower, upper, r):
        rangeString = ""
        if lower == upper:
            rangeString = str(lower)
        else:
            rangeString = f"{lower}->{upper}"
        if (len(r)>0) and rangeString != r[-1]:
            r.append(rangeString)
        else:
            r.append(rangeString)