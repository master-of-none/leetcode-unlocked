package validanagrams

import "testing"

func TestValidAnagram(t *testing.T) {
	tests := []struct {
		s        string
		t        string
		expected bool
	}{
		{"anagram", "nagaram", true},
		{"rat", "car", false},
	}

	for _, test := range tests {
		result := isAnagram(test.s, test.t)
		if result != test.expected {
			t.Errorf("For the inputs %v and %v, expected is %t, but got %t", test.s, test.t, test.expected, result)
		}
	}
}
