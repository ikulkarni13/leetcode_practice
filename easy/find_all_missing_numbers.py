class Solution:
    def findDisappearedNumbers_chad(self, nums: List[int]) -> List[int]:
        # get the length of nums to get n
        # iterate in the range from 1 to n + 1
        # check if each number is in nums
        # if it's not, add it to result array
        # return result array
        
        # O(n^2)
        # disappeared = []

        # for num in range(1, len(nums) + 1):
        #     if num not in nums:
        #         disappeared.append(num)
        
        # return disappeared

        # O(n)
        nums_set = set(nums)
        disappeared = []

        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                disappeared.append(num)

        return disappeared
    
    def findDisappearedNumbers_ira(self, nums: List[int]) -> List[int]:

        #brute force - O(n)
        #sort nums
        #create a range_dict that has all the numbers in the range
        #iterate through nums and del the found elements in range_dict
        #return unmbers left in dict as an array

        dissapeared = []
        nums_set = set(nums)

        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                dissapeared.append(num)
        
        return dissapeared

        