# -*- coding: utf-8 -*-
# @Author: 'veettier'
# @Date:   2016-10-28 10:51:37
# @Last Modified by:   'veettier'
# @Last Modified time: 2016-10-28 12:19:41

class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        length = len(nums) 
        for i in range(length):
            if target-nums[i] in nums and nums.index(target-nums[i]) != i:
                return [i, nums.index(target-nums[i])]
            i +=1


nums = [2,7,11,9]
target = 9
f = Solution()
print f.twoSum(nums, target)
