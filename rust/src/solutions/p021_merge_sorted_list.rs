use crate::util::linked_list::ListNode;

pub fn merge_two_lists(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut dummy = Some(Box::new(ListNode { val: 0, next: None }));
    let mut cur = &mut dummy;

    let (mut l1, mut l2) = (list1, list2);

    while l1.is_some() || l2.is_some() {
        if l1.is_none() {
            cur.as_mut().unwrap().next = l2;
            break;
        } else if l2.is_none() {
            cur.as_mut().unwrap().next = l1;
            break;
        }

        let next = if l1.as_ref().unwrap().val < l2.as_ref().unwrap().val {
            let (start, next) = take_head(l1);
            l1 = start;
            next
        } else {
            let (start, next) = take_head(l2);
            l2 = start;
            next
        };
        cur.as_mut().unwrap().next = next;
        cur = &mut cur.as_mut().unwrap().next;
    }

    dummy.unwrap().next
}

fn take_head(mut head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
    let head_next = head.as_mut().unwrap().next.take();
    let next = head.take();
    head = head_next;
    (head, next)
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
    #[test]
    fn test_merge_2() {
        let list1_vec: Vec<i32> = vec![];
        let list2_vec: Vec<i32> = vec![];
        let output_vec: Vec<i32> = vec![];

        let list1_head = ListNode::to_linked_list(list1_vec);
        let list2_head = ListNode::to_linked_list(list2_vec);

        let actual_head = merge_two_lists(list1_head, list2_head);
        let actual_vec = ListNode::to_vector(actual_head);

        assert_eq!(actual_vec, output_vec);
    }

    #[test]
    fn test_merge_3() {
        let list1_vec: Vec<i32> = vec![];
        let list2_vec: Vec<i32> = vec![0];
        let output_vec: Vec<i32> = vec![0];

        let list1_head = ListNode::to_linked_list(list1_vec);
        let list2_head = ListNode::to_linked_list(list2_vec);

        let actual_head = merge_two_lists(list1_head, list2_head);
        let actual_vec = ListNode::to_vector(actual_head);

        assert_eq!(actual_vec, output_vec);
    }
}
