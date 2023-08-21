"""
Merge 2 sorted list
Time Complexity: O(n)
Space Complexity: O(n)
"""

from list_node import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
        
            cur = cur.next
        
        if l1:
            cur.next = l1
        
        elif l2:
            cur.next = l2
        
        return dummy.next