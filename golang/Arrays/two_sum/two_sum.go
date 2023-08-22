package twosum

func twoSum(nums []int, target int) []int {
	hashmap := make(map[int]int)

	for i, n := range nums {
		diff := target - n

		if val, ok := hashmap[diff]; ok {
			return []int{val, i}
		}
		hashmap[n] = i
	}

	return nil
}
