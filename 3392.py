'''Given an integer array nums, return the number
of subarrays of length 3 such that the sum
of the first and third numbers equals exactly
half of the second number'''

class Solution(object):
    def countSubarrays(self, nums):
         count = 0
         for i in range(len(nums) - 2):
             if((nums[i] + nums[i+2]) * 2 == (nums[i+1])):
                 count += 1
             else:
                 count += 0
         return count