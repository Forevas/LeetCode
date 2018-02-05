'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
# solution1
class Solution1:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,n in enumerate(nums):
            m=target-n
            if m in d:
                return [d[m],i]
            else:
                d[n]=i
# solution2
class Solution2:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False;
        d={}
        for i in range(len(nums)):
            m=target-nums[i]
            if m in d:
                return [d[m],i]
            else:
                d[nums[i]]=i
s1=Solution1()
s2=Solution2()
r1=s1.twoSum([2,7,11,15],9)
r2=s2.twoSum([2,7,11,15],9)
print(r1,r2)
