// Valid Palindrome

pub fn is_palindrome(s: String) -> bool {
    let mut l = 0;
    let mut r = s.len() - 1;

    let s_chars: Vec<char> = s.chars().collect();

    while l < r {
        while l < r && !s_chars[l].is_alphanumeric(){
            l += 1;
        }
        
        while l < r && !s_chars[r].is_alphanumeric(){
            r -= 1;  
        }

        if s_chars[l].to_ascii_lowercase() != s_chars[r].to_ascii_lowercase() {
            return false;
        }

        l += 1;
        r -= 1;
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1(){
        let s = "A man, a plan, a canal: Panama";

        assert!(is_palindrome(s.to_string()));
    }

    #[test]
    fn test_case_2(){
        let s = "race a car";

        assert!(!is_palindrome(s.to_string()));
    }

    #[test]
    fn test_case_3(){
        let s = " ";

        assert!(is_palindrome(s.to_string()));
    }
}