// Product of arrays except self

pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut res: Vec<i32> = vec![1; nums.len().try_into().unwrap()];

    let mut prefix = 1;
    for i in 0..nums.len() {
        res[i] = prefix;
        prefix *= nums[i];
    }

    let mut postfix = 1;
    for i in (0..nums.len()).rev() {
        res[i] *= postfix;
        postfix *= nums[i]
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_prod_array_1() {
        let nums: Vec<i32> = vec![1, 2, 3, 4];
        let output: Vec<i32> = vec![24, 12, 8, 6];
        assert_eq!(product_except_self(nums), output)
    }

    #[test]
    fn test_prod_array_2() {
        let nums: Vec<i32> = vec![-1, 1, 0, -3, 3];
        let output: Vec<i32> = vec![0, 0, 9, 0, 0];
        assert_eq!(product_except_self(nums), output)
    }
}
