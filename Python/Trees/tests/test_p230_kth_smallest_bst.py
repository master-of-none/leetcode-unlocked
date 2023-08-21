import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p230_kth_smallest_bst import Solution

class TestSolution:
    def test_smallest_1(self):
        solution = Solution()
        input_list = [3,1,4,None,2]
        k = 1
        input_root = TreeNode.list_to_tree(input_list)

        assert solution.kthSmallest(input_root, k) == 1
    
    def test_smallest_2(self):
        solution = Solution()
        input_list = [5,3,6,2,4,None,None,1]
        k = 3
        input_root = TreeNode.list_to_tree(input_list)

        assert solution.kthSmallest(input_root, k) == 3
    
if __name__ == "__main__":
    pytest.main()