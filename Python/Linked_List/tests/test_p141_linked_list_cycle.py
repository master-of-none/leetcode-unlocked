import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from list_node import ListNode
from p141_linked_list_cycle import Solution
from typing import Optional

class TestSolution:
    def create_cycle(self, head: Optional[ListNode], pos:int) -> Optional[ListNode]:
        cycle_start = head
        cur = head
        for _ in range(pos):
            cycle_start = cycle_start.next
        
        while cur.next:
            cur = cur.next
        
        cur.next = cycle_start
        
        return head
    
    def test_reorder_1(self):
        solution = Solution()
        
        input_list = [3,2,0,-4]
        pos = 1
        input_head = ListNode.list_to_linked_list(input_list)
        input_head = TestSolution.create_cycle(self, input_head, pos)
        
        assert solution.hasCycle(input_head) == True
    
    def test_reorder_2(self):
        solution = Solution()
        
        input_list = [1, 2]
        pos = 0
        input_head = ListNode.list_to_linked_list(input_list)
        input_head = TestSolution.create_cycle(self, input_head, pos)
        
        assert solution.hasCycle(input_head) == True
        
    def test_reorder_3(self):
        solution = Solution()
        
        input_list = [1, 2, 3]
        input_head = ListNode.list_to_linked_list(input_list)
        assert solution.hasCycle(input_head) == False
        