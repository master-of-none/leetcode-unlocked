use std::collections::HashMap;

const LETTER_COUNT: usize = 26;

fn build_char_frequency(word: &str) -> [u8; LETTER_COUNT] {
    word.bytes()
        .map(|b| (b - b'a') as usize)
        .fold([0; LETTER_COUNT], |mut freq, b| {
            freq[b] += 1;
            freq
        })
}

pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    strs.into_iter()
        .map(|word| (build_char_frequency(&word), word))
        .fold(
            HashMap::<[u8; LETTER_COUNT], Vec<String>>::new(),
            |mut anagrams, (char_freq, word)| {
                anagrams.entry(char_freq).or_default().push(word);
                anagrams
            },
        )
        .into_values()
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    fn into_owned_strings(slices: Vec<&str>) -> Vec<String> {
        slices.into_iter().map(String::from).collect()
    }

    // To test correctly we need to sort
    fn sort_string_vecs(vecs: &mut Vec<Vec<String>>) {
        for vec in vecs.iter_mut() {
            vec.sort(); // Sort the strings within each group
        }
        vecs.sort_by(|a, b| a.join("").cmp(&b.join(""))); // Sort the groups
    }

    #[test]
    fn test_example_1() {
        let strs = into_owned_strings(vec!["eat", "tea", "tan", "ate", "nat", "bat"]);

        let mut expected_output = vec![vec!["bat"], vec!["nat", "tan"], vec!["ate", "eat", "tea"]]
            .into_iter()
            .map(into_owned_strings)
            .collect();

        let mut result = group_anagrams(strs);

        sort_string_vecs(&mut result);
        sort_string_vecs(&mut expected_output);

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
