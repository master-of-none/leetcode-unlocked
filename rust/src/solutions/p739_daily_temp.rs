// Daily Temperatures

pub fn daily_temp(temp: Vec<i32>) -> Vec<i32> {
    let mut res = vec![0; temp.len()];
    let mut stack: Vec<(i32, usize)> = Vec::new();

    for (i, &t) in temp.iter().enumerate() {
        while let Some((stack_t, _stack_ind)) = stack.last() {
            match t > *stack_t {
                true => {
                    let (_, stack_ind) = stack.pop().unwrap();
                    res[stack_ind] = (i - stack_ind) as i32;
                }
                false => break,
            }
        }
        stack.push((t, i));
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_daily_temp_1() {
        let input = vec![73, 74, 75, 71, 69, 72, 76, 73];
        let output = vec![1, 1, 4, 2, 1, 1, 0, 0];
        assert_eq!(daily_temp(input), output);
    }

    #[test]
    fn test_daily_temp_2() {
        let input = vec![30, 40, 50, 60];
        let output = vec![1, 1, 1, 0];
        assert_eq!(daily_temp(input), output);
    }

    #[test]
    fn test_daily_temp_3() {
        let input = vec![30, 60, 90];
        let output = vec![1, 1, 0];
        assert_eq!(daily_temp(input), output);
    }
}
