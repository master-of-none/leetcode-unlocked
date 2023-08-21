// Binary Search

pub fn search(nums: Vec<i32>, target: i32) -> i32 {
    let mut l = 0;
    let mut r = nums.len();

    while l <= r {
        let mid = l + (r - l) / 2;

        if nums[mid] < target{
            l = mid + 1
        }
        else if nums[mid] > target {
            r = mid - 1
        }

        else if nums[mid] == target {
            return mid.try_into().unwrap();
        }
    }

    -1
}

#[cfg(test)]
mod tests {
    use std::vec;

    use super::*;

    #[test]
    fn test_binary_1() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 9;
        assert_eq!(search(nums, target), 4);
    }

    #[test]
    fn test_binary_2() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 2;
        assert_eq!(search(nums, target), -1);
    }

}