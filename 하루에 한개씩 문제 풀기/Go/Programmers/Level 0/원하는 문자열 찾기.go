import "strings"

func solution(myString string, pat string) int {
    myStringLower := strings.ToLower(myString)
    patLower := strings.ToLower(pat)

    if strings.Contains(myStringLower, patLower) {
        return 1
    }

    return 0