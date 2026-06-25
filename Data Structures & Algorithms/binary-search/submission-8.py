class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or nums[-1] < target:
            return -1

        n = len(nums)/2
        index = int(n)
        while True:
            if nums[index] == target:
                return index
            elif n < 1:
                return -1
            elif nums[index] < target:
                n /= 2
                index += int(n+1)
            elif nums[index] > target:
                n /= 2
                index -= int(n+1)