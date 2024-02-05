use crate::util::linked_list::ListNode;

pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut prev: Option<Box<ListNode>> = None;
    let mut cur = head;

    while let Some(mut cur_node) = cur.take() {
        let temp = cur_node.next.take();
        cur_node.next = prev.take();
        prev = Some(cur_node);
        cur = temp;
    }
    prev
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_1() {
        let input_vector: Vec<i32> = vec![1, 2, 3, 4, 5];
        let output_vector: Vec<i32> = vec![5, 4, 3, 2, 1];

        let input_head = ListNode::to_linked_list(input_vector);

        let output_head = reverse_list(input_head);

        let actual_vector = ListNode::to_vector(output_head);

        assert_eq!(actual_vector, output_vector)
    }

    #[test]
    fn test_reverse_2() {
        let input_vector: Vec<i32> = vec![1, 2];
        let output_vector: Vec<i32> = vec![2, 1];

        let input_head = ListNode::to_linked_list(input_vector);

        let output_head = reverse_list(input_head);

        let actual_vector = ListNode::to_vector(output_head);

        assert_eq!(actual_vector, output_vector)
    }

    #[test]
    fn test_reverse_3() {
        let input_vector: Vec<i32> = vec![];
        let output_vector: Vec<i32> = vec![];

        let input_head = ListNode::to_linked_list(input_vector);

        let output_head = reverse_list(input_head);

        let actual_vector = ListNode::to_vector(output_head);

        assert_eq!(actual_vector, output_vector)
    }
}
