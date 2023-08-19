"""
Reverse Polish Notation
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
                
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif n == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
        
            elif n == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
                
            else:
                stack.append(int(n))
        
        return stack[0]