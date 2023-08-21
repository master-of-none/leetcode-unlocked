import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p1448_count_good_nodes import Solution

class TestSolution:
    def test_good_1(self):
        solution = Solution()
        input_list = [3,1,4,3,None,1,5]
        input_root = TreeNode.list_to_tree(input_list)

        actual_nodes = solution.goodNodes(input_root)

        assert actual_nodes == 4
        
    
    def test_good_2(self):
        solution = Solution()
        input_list = [3,3,None,4,2]
        input_root = TreeNode.list_to_tree(input_list)

        actual_nodes = solution.goodNodes(input_root)

        assert actual_nodes == 3
    
    
    def test_good_3(self):
        solution = Solution()
        input_list = [3]
        input_root = TreeNode.list_to_tree(input_list)

        actual_nodes = solution.goodNodes(input_root)

        assert actual_nodes == 1
        
if __name__ == "__main__":
    pytest.main()