from p155_min_stack import MinStack

class Testing:
    def test_min_stack_operations(self):
        obj = MinStack()
        assert obj.push(-2) is None
        assert obj.push(0) is None
        assert obj.push(-3) is None
        assert obj.getMin() == -3
        assert obj.pop() is None
        assert obj.top() == 0
        assert obj.getMin() == -2
