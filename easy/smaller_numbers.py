class Solution:
    def smallerNumbersThanCurrentChad(self, nums: List[int]) -> List[int]:
        # brute force O(n^2)
        # how to do a nested loop to get every combination of numbers?
        # iterate through the indices and numbers of nums (num1)
        # iterate through the indices and numbers of nums again (num2)
        # if idx2 is not equal to idx1 AND num2 is less than num1, increment counter
        # once the inner loop completes, append the counter value to res array

        # result = []
        
        # for idx1, num1 in enumerate(nums):
        #     counter = 0

        #     for idx2, num2 in enumerate(nums):
        #         if (idx2 != idx1) & (num2 < num1):
        #             counter += 1
            
        #     result.append(counter)

        # return result

        # elegant solution
        # copy the nums array
        # sort the copy array
        # map through the nums array, transforming each num to its index in sorted copy

        sorted_nums_copy = sorted(nums)
        mapped = [ sorted_nums_copy.index(num) for num in nums]
        return mapped