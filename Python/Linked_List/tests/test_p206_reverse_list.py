import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p206_reverse_list import Solution
from list_node import ListNode

class TestSolution:
    
    @pytest.fixture
    def solution(self):
        return Solution
    
    def test_reverse_list(self, solution):
        input_list = [1, 2, 3, 4, 5]
        expected_list = [5, 4, 3, 2, 1]
        
        input_head = ListNode.list_linked_list(input_list)
        
        actual_head = solution.reverse_list(self, input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)
          
        assert actual_list == expected_list

if __name__ == "__main__":
    pytest.main()