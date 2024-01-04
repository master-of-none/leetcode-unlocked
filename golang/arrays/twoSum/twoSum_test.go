package twosum

import (
	"testing"
)

func TestTwoSum(t *testing.T) {
	tests := []struct {
		nums     []int
		target   int
		expected []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}

	for _, test := range tests {
		result := twoSum(test.nums, test.target)

		equality := checkArrayEquality(result, test.expected)

		if !equality {
			t.Errorf("For the input %v, expected is %v, but got %v", test.nums, test.expected, result)
		}
	}
}

func checkArrayEquality(nums []int, expected []int) bool {
	if len(nums) != len(expected) {
		return false
	}

	for i := range nums {
		if nums[i] != expected[i] {
			return false
		}
	}
	return true
}
