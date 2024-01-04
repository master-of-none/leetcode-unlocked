use crate::util::linked_list::ListNode;

pub fn remove_nth_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
    let mut dummy = Some(Box::new(ListNode { val: 0, next: head }));
    let mut len = 0;
    {
        let mut cur = dummy.as_ref();
        while cur.unwrap().next.is_some() {
            len += 1;
            cur = cur.unwrap().next.as_ref()
        }
    }
    let n = len - n;
    {
        let mut cur = dummy.as_mut();
        for _ in 0..(n) {
            cur = cur.unwrap().next.as_mut();
        }

        let next = cur.as_mut().unwrap().next.as_mut().unwrap().next.take();
        cur.as_mut().unwrap().next = next
    }
    dummy.unwrap().next
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_1() {
        let input_list: Vec<i32> = vec![1, 2, 3, 4, 5];
        let n: i32 = 2;
        let output_list: Vec<i32> = vec![1, 2, 3, 5];

        let input_head = ListNode::to_linked_list(input_list);
        let actual_head = remove_nth_end(input_head, n);

        let actual_list = ListNode::to_vector(actual_head);

        assert_eq!(actual_list, output_list);
    }

    #[test]
    fn test_remove_2() {
        let input_list: Vec<i32> = vec![1];
        let n: i32 = 1;
        let output_list: Vec<i32> = vec![];

        let input_head = ListNode::to_linked_list(input_list);
        let actual_head = remove_nth_end(input_head, n);

        let actual_list = ListNode::to_vector(actual_head);

        assert_eq!(actual_list, output_list);
    }

    #[test]
    fn test_remove_3() {
        let input_list: Vec<i32> = vec![1, 2];
        let n: i32 = 1;
        let output_list: Vec<i32> = vec![1];

        let input_head = ListNode::to_linked_list(input_list);
        let actual_head = remove_nth_end(input_head, n);

        let actual_list = ListNode::to_vector(actual_head);

        assert_eq!(actual_list, output_list);
    }
}
