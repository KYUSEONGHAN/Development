def check_color(x: str, y: int) -> str:
    if x in ['A', 'C', 'E', 'G']:
        if y % 2 == 1:
            return 'black'
        else:
            return 'white'
    else:
        if y % 2 == 1:
            return 'white'
        else:
            return 'black'


def solution(cell1: str, cell2: str) -> bool:
    cell1_x, cell1_y = cell1[0], int(cell1[-1])
    cell2_x, cell2_y = cell2[0], int(cell2[-1])

    cell1_color = check_color(cell1_x, cell1_y)
    cell2_color = check_color(cell2_x, cell2_y)

    return cell1_color == cell2_color