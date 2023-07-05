func contains(arr []int, target int) bool {
	for _, num := range arr {
		if num == target {
			return true
		}
	}
	return false
}

func solution(myString string, indices []int) string {
	result := ""
	for i, char := range myString {
		if !contains(indices, i) {
			result += string(char)
		}
	}
	return result
}