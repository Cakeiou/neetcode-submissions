class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dictionary = dict()
        for i, num in enumerate(nums):
            num_dictionary[num] = i
        for i, num in enumerate(nums):
            if (target - num) in num_dictionary and num_dictionary[target - num] != i:
                return [i, num_dictionary[target - num]]
        
        