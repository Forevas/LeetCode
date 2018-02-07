'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
# My Solution
class Solution1:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if i>len(nums)-4:
                break
            t=target-n
            three=self._threeSum(nums[i+1:len(nums)],t)
            if three != None:
                for l in three:
                    res.append([n]+l)
        return res
    def _threeSum(self,nums,t):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            if i>len(nums)-3:
                break
            l,r=i+1,len(nums)-1
            while l<r:
                a=n+nums[l]+nums[r]
                if a<t:
                    l+=1
                elif a>t:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1;r-=1
        return res
# Better Solution
class Solution2:
    def fourSum(self,nums,target):
        def findNum(nums,target,N,result,results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N==2:
                l,r=0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        results.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l+=1;r-=1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        res=[]
        nums.sort()
        findNum(nums,target,4,[],res)
        return res
s1=Solution1()
r1=s1.fourSum([1, 0, -1, 0, -2, 2],0)
s2=Solution2()
r2=s2.fourSum([1,0,-1,0,-2,2],0)
print(r1,r2)

'''
总结：第一种方法是用了3Sum的解决方法的升级版，第二种方法主要是递归传参的时候的操作比较重要
'''
