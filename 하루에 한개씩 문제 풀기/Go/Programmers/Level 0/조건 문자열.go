func solution(ineq string, eq string, n int, m int) int {
	if ineq == "<" {
		if eq == "=" {
			if n <= m {
				return 1
			}
		} else if eq == "!" {
			if n < m {
				return 1
			}
		}
	} else if ineq == ">" {
		if eq == "=" {
			if n >= m {
				return 1
			}
		} else if eq == "!" {
			if n > m {
				return 1
			}
		}
	}
	return 0
}