#Juantamos los dos arrays, los ordenamos y vamos directamente al medio
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        position_median = len(combined)
        position_median_div = position_median // 2
        if (position_median % 2 == 0):
            return (combined[position_median_div] + combined[(position_median_div) - 1]) / 2
        else:
            return combined[position_median_div]
