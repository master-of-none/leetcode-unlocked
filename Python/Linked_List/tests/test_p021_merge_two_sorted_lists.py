import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from list_node import ListNode
from p021_merge_two_sorted_lists import Solution

class TestSolution:
    def test_merge_list_1(self):
        solution = Solution()
        
        list1 = [1,2,4]
        list2 = [1,3,4]
        
        expected_list = [1,1,2,3,4,4]
        
        l1 = ListNode.list_to_linked_list(list1)
        l2 = ListNode.list_to_linked_list(list2)
        
        actual_head = solution.mergeTwoLists(l1, l2)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
        
    def test_merge_list_2(self):
        solution = Solution()
        
        list1 = []
        list2 = []
        
        expected_list = []
        
        l1 = ListNode.list_to_linked_list(list1)
        l2 = ListNode.list_to_linked_list(list2)
        
        actual_head = solution.mergeTwoLists(l1, l2)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list
    
    def test_merge_list_3(self):
        solution = Solution()
        
        list1 = []
        list2 = [0]
        
        expected_list = [0]
        
        l1 = ListNode.list_to_linked_list(list1)
        l2 = ListNode.list_to_linked_list(list2)
        
        actual_head = solution.mergeTwoLists(l1, l2)
        actual_list = ListNode.linked_list_to_list(actual_head)
        
        assert actual_list == expected_list