// Contains Duplicates

use std::collections::HashSet;

// Uses same implemntation as python code
pub fn contains_duplicates(nums: Vec<i32>) -> bool {
    let mut hashset: HashSet<i32> = HashSet::new();

    for n in nums {
        if hashset.contains(&n) {
            return true;
        }
        hashset.insert(n);
    }
    false
}

#[cfg(test)]
pub mod tests {
    use super::*;

    #[test]
    fn test_dups_1() {
        let nums = vec![1, 2, 3, 1];
        let result = contains_duplicates(nums);
        assert_eq!(result, true);
    }

    #[test]
    fn test_dups_2() {
        let nums = vec![1, 2, 3, 4];
        let result = contains_duplicates(nums);
        assert_eq!(result, false);
    }

    #[test]
    fn test_dups_3() {
        let nums = vec![1, 2, 3, 1, 2, 3, 1, 5, 6, 2, 3];
        let result = contains_duplicates(nums);
        assert_eq!(result, true);
    }
}
