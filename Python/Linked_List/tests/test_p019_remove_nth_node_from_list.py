import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from list_node import ListNode
from p019_remove_nth_node_from_list import Solution

class TestSolution:
    def test_remove_list_1(self):
        solution = Solution()
        
        list1 = [1,2,3,4,5]
        n = 2
        
        expected_list = [1,2,3,5]
        
        l1 = ListNode.list_to_linked_list(list1)
        
        actual_head = solution.removeNthFromEnd(l1, n)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
    
    def test_remove_list_2(self):
        solution = Solution()
        
        list1 = [1]
        n = 1
        
        expected_list = []
        
        l1 = ListNode.list_to_linked_list(list1)
        
        actual_head = solution.removeNthFromEnd(l1, n)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
    
    def test_remove_list_3(self):
        solution = Solution()
        
        list1 = [1,2]
        n = 1
        
        expected_list = [1]
        
        l1 = ListNode.list_to_linked_list(list1)
        
        actual_head = solution.removeNthFromEnd(l1, n)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
        