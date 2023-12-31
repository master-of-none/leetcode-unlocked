"""
Add Numbers
Time Complexity: O(n)
Space Complexity: O(n)
"""

from list_node import ListNode
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            res = v1 + v2 + carry
            carry = res // 10
            res = res % 10
            
            cur.next = ListNode(res)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        
        return dummy.next
   