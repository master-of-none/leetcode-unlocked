use std::collections::HashMap;

pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut res: HashMap<Vec<i32>, Vec<String>> = HashMap::new();

    for s in strs.iter() {
        let mut count = vec![0; 26];

        for c in s.chars() {
            count[(c as u8 - b'a') as usize] += 1
        }
        res.entry(count).or_insert(Vec::new()).push(s.clone());
    }
    res.values().cloned().collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    // To test correctly we need to sort
    fn sort_string_vecs(mut vecs: Vec<Vec<String>>) -> Vec<Vec<String>> {
        for vec in vecs.iter_mut() {
            vec.sort(); // Sort the strings within each group
        }
        vecs.sort_by_key(|a| a.join("")); // Sort the groups
        vecs
    }

    #[test]
    fn test_anagram_1() {
        let strs = vec![
            "eat".to_string(),
            "tea".to_string(),
            "tan".to_string(),
            "ate".to_string(),
            "nat".to_string(),
            "bat".to_string(),
        ];
        let mut expected_output = vec![
            vec!["bat".to_string()],
            vec!["nat".to_string(), "tan".to_string()],
            vec!["ate".to_string(), "eat".to_string(), "tea".to_string()],
        ];

        let mut result = group_anagrams(strs);
        result = sort_string_vecs(result);
        expected_output = sort_string_vecs(expected_output);

        assert_eq!(result, expected_output);
    }

    #[test]
    fn test_anagram_2() {
        let strs = vec!["".to_string()];
        let expected_output = vec![vec!["".to_string()]];
        assert_eq!(group_anagrams(strs), expected_output);
    }

    #[test]
    fn test_anagram_3() {
        let strs = vec!["a".to_string()];
        let expected_output = vec![vec!["a".to_string()]];
        assert_eq!(group_anagrams(strs), expected_output);
    }
}
