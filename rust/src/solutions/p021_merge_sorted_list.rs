use crate::util::linked_list::ListNode;

pub fn merge_two_lists(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
}

#[cfg(test)]
mod tests {
    use std::vec;

    use super::*;

    #[test]
    fn test_merge_1() {
        let list1_vec: Vec<i32> = vec![1, 2, 4];
        let list2_vec: Vec<i32> = vec![1, 3, 4];
        let output_vec: Vec<i32> = vec![1, 1, 2, 3, 4, 4];

        let list1_head = ListNode::to_linked_list(list1_vec);
        let list2_head = ListNode::to_linked_list(list2_vec);

        let actual_head = merge_two_lists(list1_head, list2_head);
        let actual_vec = ListNode::to_vector(actual_head);

        assert_eq!(actual_vec, output_vec);
    }
}
