func solution(arr []int, k int) []int {
	uniqueNums := make(map[int]bool)
	result := []int{}

	for _, num := range arr {
		if !uniqueNums[num] {
			uniqueNums[num] = true
			result = append(result, num)
		}

		if len(result) == k {
			break
		}
	}

	for len(result) < k {
		result = append(result, -1)
	}

	return result
}