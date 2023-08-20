import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from list_node import ListNode
from p206_reverse_list import Solution
class TestSolution:
    def test_reverse_list_1(self):
        solution = Solution()
        input_list = [1, 2, 3, 4, 5]
        expected_list = [5, 4, 3, 2, 1]

        input_head = ListNode.list_to_linked_list(input_list)

        actual_head = solution.reverse_list(input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)

        assert actual_list == expected_list

    def test_reverse_list_2(self):
        solution = Solution()
        input_list = [1, 2]
        expected_list = [2, 1]

        input_head = ListNode.list_to_linked_list(input_list)

        actual_head = solution.reverse_list(input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)

        assert actual_list == expected_list

    def test_reverse_list_3(self):
        solution = Solution()
        input_list = []
        expected_list = []

        input_head = ListNode.list_to_linked_list(input_list)

        actual_head = solution.reverse_list(input_head)
        actual_list = ListNode.linked_list_to_list(actual_head)

        assert actual_list == expected_list


if __name__ == "__main__":
    pytest.main()
