import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p049_group_anagrams import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        strs = ["eat","tea","tan","ate","nat","bat"]
        output = [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        # Converting dict_values to a list of lists for comparison
        actual_output = solution.groupAnagrams(strs)
        
        # Sorting the inner lists for both expected and actual output
        sorted_expected = [sorted(group) for group in output]
        sorted_actual = [sorted(group) for group in actual_output]
        
        # Sorting the list of groups for both expected and actual output
        sorted_expected.sort()
        sorted_actual.sort()
        
        assert sorted_actual == sorted_expected
    
    def test_example_2(self):
        solution = Solution()
        strs = [""]
        output = [[""]]
        assert list(solution.groupAnagrams(strs)) == output
    
    def test_example_3(self):
        solution = Solution()
        strs = ["a"]
        output = [["a"]]
        assert list(solution.groupAnagrams(strs)) == output

if __name__ == "__main__":
    pytest.main()
