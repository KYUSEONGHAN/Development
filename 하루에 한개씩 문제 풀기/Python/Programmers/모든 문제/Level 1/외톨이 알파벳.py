def solution(input_string: str) -> str:
    dict = {}

    for index, alpa in enumerate(input_string):
        if alpa not in dict:
            dict[alpa] = 1
        else:
            if input_string[index - 1] != alpa:
                dict[alpa] += 1

    l = [key for key, value in dict.items() if value >= 2]

    return ''.join(map(str, sorted(l))) if l else 'N'git