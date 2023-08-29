#[derive(Debug, PartialEq)]
pub struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

impl ListNode {
    pub fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }

    pub fn insert(&mut self, val: i32) {
        if let Some(ref mut next_node) = self.next {
            next_node.insert(val);
        } else {
            self.next = Some(Box::new(ListNode::new(val)));
        }
    }

    pub fn to_linked_list(lst: Vec<i32>) -> Option<Box<ListNode>> {
        if lst.is_empty() {
            return None;
        }

        let mut head = Some(Box::new(ListNode::new(lst[0])));
        let mut cur = head.as_mut();

        for &val in &lst[1..] {
            if let Some(node) = cur {
                node.insert(val);
                cur = node.next.as_mut();
            }
        }
        head
    }

    pub fn to_vector(node: Option<Box<ListNode>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut current = node.as_deref();

        while let Some(val) = current {
            result.push(val.val);
            current = val.next.as_deref();
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_insert() {
        let mut head: ListNode = ListNode::new(1);
        head.insert(2);
        head.insert(3);

        let expected_result: Vec<i32> = vec![1, 2, 3];
        let actual_result: Vec<i32> = ListNode::to_vector(Some(Box::new(head)));

        assert_eq!(actual_result, expected_result);
    }

    #[test]
    fn test_to_linked_list() {
        let vec = vec![1, 2, 3, 4, 5];
        let lst = ListNode::to_linked_list(vec.clone());
        let lst_values = ListNode::to_vector(lst);
        assert_eq!(lst_values, vec);
    }

    #[test]
    fn test_to_vector() {
        let lst = ListNode::to_linked_list(vec![1, 2, 3, 4, 5]);
        let expected_result: Vec<i32> = vec![1, 2, 3, 4, 5];
        let actual_result: Vec<i32> = ListNode::to_vector(lst);
        assert_eq!(actual_result, expected_result);
    }

    #[test]
    fn test_to_vector_empty_list() {
        let empty_list: Option<Box<ListNode>> = None;
        let expected_result: Vec<i32> = Vec::new();
        let actual_result: Vec<i32> = ListNode::to_vector(empty_list);
        assert_eq!(actual_result, expected_result);
    }

    #[test]
    fn test_to_linked_list_empty_vector() {
        let empty_vec: Vec<i32> = Vec::new();
        let expected_result: Option<Box<ListNode>> = None;
        let actual_result: Option<Box<ListNode>> = ListNode::to_linked_list(empty_vec);
        assert_eq!(actual_result, expected_result);
    }
}
