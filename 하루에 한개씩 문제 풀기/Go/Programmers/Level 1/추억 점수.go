// 2023.06.05
func solution(name []string, yearning []int, photo [][]string) []int {
    m := make(map[string]int)

	for i, p := range name {
        m[p] = yearning[i]
    }

    s := make([]int, len(photo))

	for i, pic := range photo {
        for _, p := range pic {
            s[i] += m[p]
        }
    }

    return s
}