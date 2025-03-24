class Solution:
    def hasCycleChad(self, head: Optional[ListNode]) -> bool:
        # time complexity: O(n)
        # nodes_set = set()

        # while head:
        #     if head in nodes_set:
        #         return True

        #     nodes_set.add(head)
        #     head = head.next
        
        # return False
    
        # time complexity: (1)
        if head == None:
            return False
        
        slow = head
        fast = head

        while head:
            if fast.next == None or fast.next.next == None:
                return False

            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

