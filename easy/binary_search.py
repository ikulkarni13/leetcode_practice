# assign left and right pointers to 0 and nums length - 1 indices
# while left is not equal to right
# divide nums length by 2 (rounded up)
# if target is in the array (sliced from rounded to nums length)
# reassign left to rounded
# else reassign right to rounded minus 1
# after loop, return -1


class Solution:
    def searchChad(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle

        return -1