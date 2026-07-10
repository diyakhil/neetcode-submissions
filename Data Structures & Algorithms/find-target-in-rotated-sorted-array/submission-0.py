class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            print(mid)

            if target == nums[mid]:
                return mid
            #need to compare nums[mid] against nums[right] first to see what array we are in
            
            #we are in smaller half of the array RIGHT
            if nums[mid] <= nums[right]:
                #we are in correct half of the array, but our value is greater than mid so we must move left pointer up so we explore greater values
                if target > nums[mid] and target <= nums[right]: 
                    left = mid + 1
                else:
                    right = mid - 1
                    
            
            #we are in larger half of the array LEFT
            else:
                #target is also in larger half of array

                #we are in correct half of array but our value is smaller, so we mist shift further down
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
        