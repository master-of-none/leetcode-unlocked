"""
Reorder List
Time Complexity: O(n)
Space Complexity: O(1)
"""

from list_node import ListNode
from typing import Optional

class Solution:
    def reorder(self, head:Optional[ListNode]) -> Optional[ListNode]:
        # Test Case not present, but added for clarity
        if not head:
            return None
        
        slow = head
        fast = head.next
        
        # Find Middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        
        # Reverse Second Part
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge 2 lists
        second = prev
        first = head
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        return head
        