package validanagram

import "testing"

func TestIsAnagram(t *testing.T) {
	tests := [] struct {
		s string
		t string
		expected bool
	}{
		{"anagram", "nagaram", true},
		{"rat", "car", false},
	}

	for _, test := range tests {
		t.Run(test.s + "_" +test.t, func(t *testing.T) {
			result := isAnagram(test.s, test.t)

			if result != test.expected {
				t.Errorf("For %s and %s, expected %v, but %v is present", test.s, test.t,test.expected, result)
			}
		})
	}
}