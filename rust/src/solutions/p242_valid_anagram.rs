// Valid Anagram using 2 hashmaps
use std::collections::HashMap;

pub fn is_anagram(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }
    let mut count_s: HashMap<char, i32> = HashMap::new();
    let mut count_t: HashMap<char, i32> = HashMap::new();

    for i in 0..s.len() {
        *count_s.entry(s.chars().nth(i).unwrap()).or_insert(0) += 1;
        *count_t.entry(t.chars().nth(i).unwrap()).or_insert(0) += 1;
    }

    count_s == count_t
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_anagram_1() {
        let s = String::from("anagram");
        let t = String::from("nagaram");
        assert_eq!(is_anagram(s, t), true);
    }

    #[test]
    fn test_anagram_2() {
        let s = String::from("rat");
        let t = String::from("car");
        assert_eq!(is_anagram(s, t), false);
    }
}
