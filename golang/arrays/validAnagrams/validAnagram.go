package validanagrams

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	countS := make(map[rune]int)
	countT := make(map[rune]int)

	for _, c := range s {
		countS[c] = 1 + countS[c]
	}

	for _, c := range t {
		countT[c] = 1 + countT[c]
	}

	for key, value := range countS {
		if countT[key] != value {
			return false
		}
	}
	return true
}
