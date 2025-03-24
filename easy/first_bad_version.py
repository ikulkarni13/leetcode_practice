class Solution:
    def firstBadVersionChad(self, n: int) -> int:
        # uses binary serach algo. t-complex is O(logn)
        left = 1
        right = n

        while left < right:
            middle = (left + right) // 2

            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        
        return left
