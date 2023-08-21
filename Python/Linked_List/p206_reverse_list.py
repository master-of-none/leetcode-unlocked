"""
Reverse a linked list
Time Complexity: O(n)
Space Complexity: O(n)
"""

from list_node import ListNode
from typing import Optional

class Solution:
    def reverse_list(self, head:Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev