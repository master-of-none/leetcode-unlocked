use std::collections::HashMap;
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = HashMap::with_capacity(nums.len());
    for (i, n) in nums.iter().enumerate() {
        let diff = target - n;

        match map.get(&(diff)) {
            None => {
                map.insert(n, i);
            }
            Some(index) => return vec![*index as i32, i as i32],
        }
    }
    vec![]
}

// submission codes end

#[cfg(test)]
pub mod tests {
    use super::*;

    #[test]
    fn test_two_sum_1() {
        assert_eq!(vec![0, 1], two_sum(vec![2, 7, 11, 15], 9));
        assert_eq!(vec![1, 2], two_sum(vec![3, 2, 4], 6));
    }
}
