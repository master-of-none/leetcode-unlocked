import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from list_node import ListNode
from p002_add_numbers import Solution

class TestSolution:
    def test_add_1(self):
        solution = Solution()
        
        list1 = [2,4,3]
        list2 = [5,6,4]
        
        expected_list = [7,0,8]
        
        l1 = ListNode.list_to_linked_list(list1)
        l2 = ListNode.list_to_linked_list(list2)
        
        actual_head = solution.addTwoNumbers(l1, l2)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
    
    def test_add_2(self):
        solution = Solution()
        
        list1 = [0]
        list2 = [0]
        
        expected_list = [0]
        
        l1 = ListNode.list_to_linked_list(list1)
        l2 = ListNode.list_to_linked_list(list2)
        
        actual_head = solution.addTwoNumbers(l1, l2)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
        
    def test_add_3(self):
        solution = Solution()
        
        list1 = [9,9,9,9,9,9,9]
        list2 = [9,9,9,9]
        
        expected_list = [8,9,9,9,0,0,0,1]
        
        l1 = ListNode.list_to_linked_list(list1)
        l2 = ListNode.list_to_linked_list(list2)
        
        actual_head = solution.addTwoNumbers(l1, l2)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list