'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1,l2=len(nums1),len(nums2)
        if l1>l2:
            l1,l2,nums1,nums2=l2,l1,nums2,nums1
        imin,imax,halfL=0,l1,(l1+l2+1)//2
        while imin<=imax:
            i=(imin+imax)//2
            j=halfL-i
            if i<l1 and nums1[i]<nums2[j-1]:
                imin=i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if i==0:
                    max_left=nums2[j-1]
                elif j==0:
                    max_left=nums1[i-1]
                else:
                    max_left=max(nums1[i-1],nums2[j-1])

                if (l1+l2)%2==1:
                    return max_left

                if i==l1:
                    min_right=nums2[j]
                elif j==l2:
                    min_right=nums1[i]
                else:
                    min_right=min(nums1[i],nums2[j])

                return (max_left+min_right)/2


num1=[1,3]
num2=[2]
s=Solution()
r=s.findMedianSortedArrays(num1,num2)
print(r)

'''
数组均已排过序，从小到大排列，所以我们要求两个数组的中位数，一般来说需要将两个数组进行归并排序后才可以得到中位数，不过这种方法的时间复杂度比较高，
因此，这里不用这种方式。
这里我们可以使用数组分割的方式，将数组1和数组2分别分割为两部分，那么数组1的左半部分+数组2的左半部分应该等于数组1和2的右半部分的元素的个数，
我们可以得到数组1和2分割点的关系，然后使用二分法，在数组1中进行查找，找到某个分割点，使得右半部分总比左半部分的任意一个元素大，如此即可找到中位数。
'''



