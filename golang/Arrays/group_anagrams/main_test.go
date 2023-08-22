package main

import (
	"reflect"
	"sort"
	"testing"
)

func TestGroupAnagrams(t *testing.T) {
	testCases := []struct {
		input    []string
		expected [][]string
	}{
		{
			input:    []string{"eat", "tea", "tan", "ate", "nat", "bat"},
			expected: [][]string{{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}},
		},
		{
			input:    []string{""},
			expected: [][]string{{""}},
		},
		{
			input:    []string{"a"},
			expected: [][]string{{"a"}},
		},
	}

	for _, tc := range testCases {
		output := groupAnagrams(tc.input)
		for _, group := range output {
			sort.Strings(group) // Sort the strings within each group
		}
		sort.Slice(output, func(i, j int) bool {
			return len(output[i]) < len(output[j]) // Sort groups by size
		})
		sort.Slice(tc.expected, func(i, j int) bool {
			return len(tc.expected[i]) < len(tc.expected[j])
		})

		if !reflect.DeepEqual(output, tc.expected) {
			t.Errorf("For input %v, expected %v, but got %v", tc.input, tc.expected, output)
		}
	}
}
