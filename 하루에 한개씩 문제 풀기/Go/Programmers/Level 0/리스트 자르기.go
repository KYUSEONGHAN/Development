func solution(n int, slicer []int, numList []int) []int {
	a, b, c := slicer[0], slicer[1], slicer[2]

	switch n {
	case 1:
		return numList[:b+1]
	case 2:
		return numList[a:]
	case 3:
		return numList[a : b+1]
	case 4:
		var result []int
		for i := a; i <= b; i += c {
			result = append(result, numList[i])
		}
		return result
	}

	return nil
}