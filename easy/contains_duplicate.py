class Solution:
    def containsDuplicate_chad(self, nums: List[int]) -> bool:
        # O(n) idea
        # iterate through the nums array, adding each value to a hash
        # if the value already exists within the hash, we found a duplicate and return true
        # once the entire search is complete, no duplicate has been found, return false

        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        
        return False
    
    def containsDuplicate_ira(self, nums: List[int]) -> bool:

        #O(n)
        #iterate through the list and add elements of the list to a dict
        #if the element exists in the list return true
        #if not, add it to the list and make value 1
        # at the end of the iteration if all the values in the dict are 1 return false

        dict_count = {}

        for num in nums:
            if num in dict_count:
                return True
            else:
                dict_count[num] = 1
        
        return False

        #brute force - O(n^2)
        #iterate through nums in the outer for loop
        #inner for loop iterates over the rest of the elements to check if the current element exists
        #if loop complete return false

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
            
        return False
    
