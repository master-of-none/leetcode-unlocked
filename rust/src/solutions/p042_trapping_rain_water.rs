pub fn trap(height: Vec<i32>) -> i32 {
    let mut res: i32 = 0;
    let mut l = 0;
    let mut r = height.len() - 1;
    let mut left_max = height[l];
    let mut right_max = height[r];

    while l < r {
        if left_max < right_max {
            l += 1;
            left_max = left_max.max(height[l]);
            res += left_max - height[l];
        } else {
            r -= 1;
            right_max = right_max.max(height[r]);
            res += right_max - height[r];
        }
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_trap_1() {
        let height: Vec<i32> = vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
        let output: i32 = 6;

        assert_eq!(trap(height), output)
    }

    #[test]
    fn test_trap_2() {
        let height: Vec<i32> = vec![4, 2, 0, 3, 2, 5];
        let output: i32 = 9;

        assert_eq!(trap(height), output)
    }
}
