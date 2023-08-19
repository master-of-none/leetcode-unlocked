// Valid Parantheses

pub fn valid_parantheses(s: String) -> bool {
    let mut stack: Vec<char> = Vec::new();
    let hashmap: std::collections::HashMap<char, char> = [(')', '('), ('}', '{'), (']', '[')]
        .iter()
        .cloned()
        .collect();

    for c in s.chars() {
        if hashmap.contains_key(&c) {
            if let Some(top) = stack.last() {
                if *top == *hashmap.get(&c).unwrap() {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            stack.push(c)
        }
    }
    stack.is_empty()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_1() {
        let s = "()".to_string();
        assert!(valid_parantheses(s))
    }

    #[test]
    fn test_valid_2() {
        let s = "()[]{}".to_string();
        assert!(valid_parantheses(s))
    }

    #[test]
    fn test_valid_3() {
        let s = "()]}".to_string();
        assert!(!valid_parantheses(s))
    }
}
