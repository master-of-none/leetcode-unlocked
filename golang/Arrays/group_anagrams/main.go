package main

import (
	"fmt"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	res := make(map[string][]string)

	for _, s := range strs {
		count := make([]int, 26)

		for _, c := range s {
			count[c-'a']++
		}

		countStr := intToString(count)
		res[countStr] = append(res[countStr], s)
	}

	var result [][]string
	for _, v := range res {
		result = append(result, v)
	}

	return result
}

func intToString(nums []int) string {
	strNums := make([]string, len(nums))

	for i, num := range nums {
		strNums[i] = fmt.Sprint(num)
	}
	return strings.Join(strNums, "#")
}
