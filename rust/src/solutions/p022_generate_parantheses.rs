// Genrate paratheses using backtracking

pub fn generate_parantheses(n: i32) -> Vec<String> {
    let mut stack = Vec::new();
    let mut result = Vec::new();

    fn backtrack(stack: &mut Vec<char>, result: &mut Vec<String>, open: i32, close: i32, n: i32) {
        if open == n && close == n {
            result.push(stack.iter().collect());
            return;
        }

        if open < n {
            stack.push('(');
            backtrack(stack, result, open + 1, close, n);
            stack.pop();
        }

        if close < open {
            stack.push(')');
            backtrack(stack, result, open, close + 1, n);
            stack.pop();
        }
    }

    backtrack(&mut stack, &mut result, 0, 0, n);
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_par_1() {
        let n = 3;
        let output = vec!["((()))", "(()())", "(())()", "()(())", "()()()"];

        assert_eq!(generate_parantheses(n), output);
    }

    #[test]
    fn test_generate_par_2() {
        let n = 1;
        let output = vec!["()"];

        assert_eq!(generate_parantheses(n), output);
    }
}
