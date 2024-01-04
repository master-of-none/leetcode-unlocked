package containsDuplicate

import "testing"

func TestContainsDuplicate(t *testing.T) {
	tests := []struct {
		nums     []int
		expected bool
	}{
		{[]int{1, 2, 3, 1}, true},
		{[]int{1, 2, 3, 4}, false},
	}

	for _, test := range tests {
		result := containsDuplicate(test.nums)
		if result != test.expected {
			t.Errorf("For the input %v, expected is %t, but got %t", test.nums, test.expected, result)
		}
	}
}
