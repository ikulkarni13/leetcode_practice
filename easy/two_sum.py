class Solution:
    def twoSum_ira(self, nums: List[int], target: int) -> List[int]:
        
        #O(N^2) - Brute Force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


        # iterate through nums
        # get comlements (target - element)
        # store complements in dictionary (complement:index)
        # iterate thru array again
        # for each element, check if complement exists in dict

        #O(N) - optimal
        complements = {}

        for index, num in enumerate(nums):
            
            if num in complements:
                return [index, complements[num]]
            else:
                complements[target-num] = index

