class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = []

        #have 2 diff pointers for each array, increment the one that we add to the array
        nums1_p = 0
        nums2_p = 0
        
        while nums1_p < len(nums1) and nums2_p < len(nums2):
            if nums1[nums1_p] <= nums2[nums2_p]:
                sorted_arr.append(nums1[nums1_p])
                nums1_p += 1
            else:
                sorted_arr.append(nums2[nums2_p])
                nums2_p += 1
        
        #append leftover to the end, leftover could be in nums1 or nums2
        while nums1_p < len(nums1):
            sorted_arr.append(nums1[nums1_p])
            nums1_p += 1
        
        while nums2_p < len(nums2):
            sorted_arr.append(nums2[nums2_p])
            nums2_p += 1
        
        #calculate median

        #if we have odd number of elements, median will just be the middle value
        #if we have an even number, then median will be average of middle 2 values

        if len(sorted_arr) % 2 == 1:
            mid_index = len(sorted_arr) // 2
            return sorted_arr[mid_index]
        else:
            mid_index = len(sorted_arr) // 2
            i = mid_index - 1
            return (sorted_arr[mid_index] + sorted_arr[i]) / float(2)
        