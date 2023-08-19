// Two sum sorted

pub fn two_sum(numbers: Vec<i32>, target:i32) -> Vec<i32> {
    let mut l = 0;
    let mut r = numbers.len() - 1;

    while l < r {
        let temp = numbers[l] + numbers[r];

        if temp < target {
            l += 1;
        }
        else if temp > target {
            r -= 1;
        }
        else {
            return vec![(l+1) as i32, (r+1) as i32];
        }
    }
    vec![]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1() {
        let numbers = vec![2, 7, 11, 15];
        let target = 9;
        let result = two_sum(numbers.clone(), target);
        assert_eq!(result, vec![1, 2]);
    }

    #[test]
    fn test_case_2() {
        let numbers = vec![2, 3, 4];
        let target = 6;
        let result = two_sum(numbers.clone(), target);
        assert_eq!(result, vec![1, 3]);
    }

    #[test]
    fn test_case_3() {
        let numbers = vec![-1, 0];
        let target = -1;
        let result = two_sum(numbers.clone(), target);
        assert_eq!(result, vec![1, 2]);
    }
}
