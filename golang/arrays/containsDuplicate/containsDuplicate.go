package containsDuplicate

func containsDuplicate(nums []int) bool {
	hashset := make(map[int]bool)

	for _, i := range nums {
		if _, ok := hashset[i]; ok {
			return true
		}
		hashset[i] = true
	}
	return false
}
