use crate::util::linked_list::ListNode;

pub fn merge_two_lists(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode::new(0));
    let mut cur = &mut dummy;

    let (mut l1, mut l2) = (list1, list2);

    while let (Some(mut node1), Some(mut node2)) = (l1.take(), l2.take()) {
        if node1.val < node2.val {
            let next_node = node1.next.take();
            cur.next = Some(node1);
            l1 = next_node;
        } else {
            let next_node = node2.next.take();
            cur.next = Some(node2);
            l2 = next_node;
        }
        cur = cur.next.as_mut().unwrap();
    }

    cur.next = l1.or(l2);
    dummy.next
}
