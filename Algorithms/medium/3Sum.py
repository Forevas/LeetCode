'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            if i>len(nums)-3:
                break
            l,r=i+1,len(nums)-1
            while l<r:
                a=n+nums[l]+nums[r]
                if a<0:
                    l+=1
                elif a>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1;r-=1
        return res

s=Solution()
r=s.threeSum([-1,0,1,2,-1,-4])
print(r)

'''
总结:这道题思路是先排序,然后从0开始遍历到倒数第3个数
对于每次遍历,分别取l为当前下标加1,r为倒数第一个下标,利用当前位置的元素+l元素+r元素进行判断,
l++或者r--,正确的答案加入list,注意l和r位置去重.最后返回答案
'''

