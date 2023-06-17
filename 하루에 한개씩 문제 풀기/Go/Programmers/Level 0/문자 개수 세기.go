func solution(myString string) []int {
	counts := make([]int, 52)

	for _, char := range myString {
		if char >= 'A' && char <= 'Z' {
			counts[char-'A']++
		} else if char >= 'a' && char <= 'z' {
			counts[char-'a'+26]++
		}
	}

	return counts
}