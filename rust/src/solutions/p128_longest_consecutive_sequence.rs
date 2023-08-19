use std::collections::HashSet;

pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
    let hashset: HashSet<i32> = nums.iter().cloned().collect();
    let mut res = 0;

    for &n in &nums {
        if !hashset.contains(&(n - 1)) {
            let mut length = 0;
            while hashset.contains(&(n + length)) {
                length += 1
            }
            res = res.max(length);
        }
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_longest_cons_1() {
        let nums = vec![100, 4, 200, 1, 3, 2];
        assert_eq!(longest_consecutive(nums), 4);
    }

    #[test]
    fn test_longest_cons_2() {
        let nums = vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1];
        assert_eq!(longest_consecutive(nums), 9);
    }
}
