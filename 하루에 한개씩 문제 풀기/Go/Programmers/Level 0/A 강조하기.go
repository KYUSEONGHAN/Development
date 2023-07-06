import (
    "strings"
    "unicode"
)

func solution(myString string) string {
	result := strings.Builder{}
	for _, char := range myString {
		if char == 'a' {
			result.WriteString("A")
		} else if unicode.IsUpper(char) && char != 'A' {
			result.WriteString(strings.ToLower(string(char)))
		} else {
			result.WriteString(string(char))
		}
	}
	return result.String()
}