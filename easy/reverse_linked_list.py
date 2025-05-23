class Solution:
    def reverseListChad(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        return prev