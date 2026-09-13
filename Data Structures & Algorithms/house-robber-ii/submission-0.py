class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        robfirst_nums = nums[:-1]
        roblast_nums = nums[1:]

        val1, val2 = 0, 0

        for num in robfirst_nums:
            temp = max(num + val1, val2)
            val1 = val2
            val2 = temp

        robfirst = val2

        val1, val2 = 0, 0

        for num in roblast_nums:
            temp = max(num + val1, val2)
            val1 = val2
            val2 = temp

        roblast = val2

        return max(robfirst, roblast)