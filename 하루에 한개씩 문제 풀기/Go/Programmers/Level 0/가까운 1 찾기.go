func solution(arr []int, idx int) int {
    for i := idx; i < len(arr); i++ {
        if arr[i] == 1 {
            return i
        }
    }
    return -1
}