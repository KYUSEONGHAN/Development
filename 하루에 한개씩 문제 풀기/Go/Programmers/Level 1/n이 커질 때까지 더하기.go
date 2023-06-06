func solution(numbers []int, n int) int {
    result := 0

    for num := 0; num <= len(numbers); num ++ {
        result += numbers[num]

        if result > n {
            break
        }
    }

    return result
}