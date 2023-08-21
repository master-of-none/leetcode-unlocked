"""
Searching 2D matrix
Time Complexity: O(logn)
Space Complexity: O(n)
"""

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top = 0
        bot = ROWS - 1
        
        while top <= bot:
            row = (top + bot) // 2
            
            if matrix[row][-1] < target:
                top = row + 1
            
            elif matrix[row][0] > target:
                bot = row - 1
            
            else:
                break
            
            if not (top <= bot):
                return False
            
        
        row = (top + bot) // 2
        l = 0
        r = COLS - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if matrix[row][m] < target:
                l = m + 1
            
            elif matrix[row][m] > target:
                r = m - 1
            
            else:
                return True
        
        return False