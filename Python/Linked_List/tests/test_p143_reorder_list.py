import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from list_node import ListNode
from p143_reorder_list import Solution

class TestSolution:
    def test_reorder_1(self):
        solution = Solution()
        
        input_list = [1,2,3,4]
        expected_list = [1,4,2,3]
        
        input_head = ListNode.list_to_linked_list(input_list)
        actual_head = solution.reorder(input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
        
    def test_reorder_2(self):
        solution = Solution()
        
        input_list = [1,2,3,4,5]
        expected_list = [1,5,2,4,3]
        
        input_head = ListNode.list_to_linked_list(input_list)
        actual_head = solution.reorder(input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
    
    def test_reorder_3(self):
        solution = Solution()
        
        input_list = []
        expected_list = []
        
        input_head = ListNode.list_to_linked_list(input_list)
        actual_head = solution.reorder(input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
        