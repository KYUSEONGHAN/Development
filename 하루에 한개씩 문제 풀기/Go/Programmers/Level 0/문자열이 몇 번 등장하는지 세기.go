func solution(myString string, pat string) int {
    count := 0

    for i := 0; i <= len(myString)-len(pat); i++ {
        if myString[i:i+len(pat)] == pat {
            count++
        }
    }

    return count
}