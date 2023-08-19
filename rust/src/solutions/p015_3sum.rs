pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut res: Vec<Vec<i32>> = Vec::new();

    let mut nums = nums.clone();
    nums.sort();

    for i in 0..nums.len() {
        if i > 0 && nums[i] == nums[i - 1] {
            continue;
        }
        let mut l = i + 1;
        let mut r = nums.len() - 1;

        while l < r {
            let temp = nums[i] + nums[l] + nums[r];

            if temp < 0 {
                l += 1;
            } else if temp > 0 {
                r -= 1;
            } else {
                res.push(vec![nums[i], nums[l], nums[r]]);
                l += 1;
                r -= 1;

                while l < r && nums[l] == nums[l - 1] {
                    l += 1;
                }
            }
        }
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_3sum_1() {
        let nums = vec![-1, 0, 1, 2, -1, -4];
        let result = three_sum(nums);
        let expected = vec![vec![-1, -1, 2], vec![-1, 0, 1]];
        assert_eq!(result, expected);
    }

    #[test]
    fn test_3sum_2() {
        let nums = vec![0, 1, 1];
        let result = three_sum(nums);
        let expected: Vec<Vec<i32>> = Vec::new();
        assert_eq!(result, expected);
    }

    #[test]
    fn test_3sum_3() {
        let nums = vec![0, 0, 0];
        let result = three_sum(nums);
        let expected = vec![vec![0, 0, 0]];
        assert_eq!(result, expected);
    }
}
