'''
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
# Approach 1: Two hashtables
from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        
        res = []
        for k in nums1_count:
            if k in nums2_count:
                res += [k]*min(nums1_count[k], nums2_count[k])
        
        return res

# Approach 2: One hashtable
# Let's optimize our space consumption, as we only need one hashtable
# Time complexity O(n+m) where n, m are lengths of two arrays
# Space complexity O(min(n,m)) - hashtable for the smaller array
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # pick the smaller array to create a hashmap for it
        if (len(nums1) > len(nums2)):
            return self.intersect(nums2, nums1)
        
        # create a hashtable of counts of the shorter array
        hashtable = defaultdict(int)
        for num in nums1:
            hashtable[num] += 1
        
        # interate over the second array
        # we can reuse nums1 to store the output to minimize space consumption
        k = 0
        for num in nums2:
            if num in hashtable and hashtable[num] > 0:
                nums1[k] = num
                hashtable[num] -= 1
                k += 1
        
        return nums1[:k]

# Approach 3: Sort + Two pointers
# If the original arrays aren't sorted, the sorting bumps the time complexity to O(nlog(n) + mlog(m))
# Space complexity is O(log(n) + log(m)) or O(n + m) depending on sort implementation
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = k = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]



        

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
obj.intersect(nums1, nums2)







import bisect
def exists(a,x):
    i = bisect.bisect_left(a,x)
    if i != len(a) and a[i] == x:
        return True
    return False