from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        """
        nums_dict = dict()
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums_dict:
                return [nums_dict[dif], i]
            nums_dict[nums[i]] = i
