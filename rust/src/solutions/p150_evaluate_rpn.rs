// Evaluate Reverse Polish Notation using patter matching

pub fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut stack: Vec<i32> = Vec::new();

    for c in tokens.iter() {
        match c.as_str() {
            "+" => {
                let a = stack.pop().unwrap();
                let b = stack.pop().unwrap();
                stack.push(a + b);
            }

            "*" => {
                let a = stack.pop().unwrap();
                let b = stack.pop().unwrap();
                stack.push(a * b);
            }

            "-" => {
                let a = stack.pop().unwrap();
                let b = stack.pop().unwrap();
                stack.push(b - a);
            }

            "/" => {
                let a = stack.pop().unwrap();
                let b = stack.pop().unwrap();
                stack.push(b / a);
            }
            _ => {
                stack.push(c.parse::<i32>().unwrap())
            }
        }
    }

    stack.pop().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn into_owned_strings(slices: Vec<&str>) -> Vec<String> {
        slices.into_iter().map(String::from).collect()
    }

    #[test]
    fn test_eval_rpn_1() {
        let tokens: Vec<String> = into_owned_strings(vec!["2","1","+","3","*"]);
        assert_eq!(eval_rpn(tokens),9)
    }

    #[test]
    fn test_eval_rpn_2() {
        let tokens: Vec<String> = into_owned_strings(vec!["4","13","5","/","+"]);
        assert_eq!(eval_rpn(tokens),6)
    }

    #[test]
    fn test_eval_rpn_3() {
        let tokens: Vec<String> = into_owned_strings(vec!["10","6","9","3","+","-11","*","/","*","17","+","5","+"]);
        assert_eq!(eval_rpn(tokens),22)
    }
}