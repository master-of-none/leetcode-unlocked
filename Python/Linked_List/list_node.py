# from typing import Optional, Self
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        
    def insert(self, val):
        new_node = ListNode(val)
        new_node.next = self.next
        self.next = new_node

    # @classmethod
    # def from_list(cls, list_) -> Optional[Self]:
    #     if not list_:
    #         return None

    #     if len(list_) == 1:
    #         return cls(list_[0], None)

    #     return cls(list_[0], cls.from_list(list_[1:]))
    
    @staticmethod
    def list_to_linked_list(lst):
        if not lst:
            return None
        
        head = ListNode(lst[0])
        cur = head
        
        for val in lst[1:]:
            cur.insert(val)
            cur = cur.next
        
        return head

    def __str__(self) -> str:
        temp = self
        vals = []

        while temp:
            vals.append(str(temp.val))
            temp = temp.next

        return ' -> '.join(vals)
    
    @staticmethod
    def linked_list_to_list(head):
        result_list = []
        cur = head
        
        while cur:
            result_list.append(cur.val)
            cur = cur.next
        
        return result_list
        