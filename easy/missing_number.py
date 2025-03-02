class Solution:
    def missingNumber_ira(self, nums: List[int]) -> int:

        #brute force - O(n^2)
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i

        #O(n)
        n = len(nums)
        range_dict = {i: "" for i in range(n+1)}
        print(range_dict)

        for num in nums:
            range_dict.pop(num, None)
        
        return next(iter(range_dict))
    
        #O(n)
        return (sum(range(len(nums)+1)) - sum(nums))