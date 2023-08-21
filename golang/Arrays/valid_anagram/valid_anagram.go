package validanagram

func isAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	countS := make(map[rune]int)
	countT := make(map[rune]int)

	for _, ch := range s {
		countS[ch] = 1 + countS[ch]
	}

	for _, ch := range t {
		countT[ch] = 1 + countT[ch]
	}

	for ch, count := range countS {
		if countT[ch] != count {
			return false
		}
	}

	return true

}