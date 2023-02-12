def get_skip_alphabet_list(skip):
    return [chr(alpha_num) for alpha_num in range(ord('a'), ord('z') + 1) if chr(alpha_num) not in skip]


def shift_alphabet(alphabet, index, skip_alphabet_list):
    skip_alpha_len = len(skip_alphabet_list)
    return skip_alphabet_list[(skip_alphabet_list.index(alphabet) + index) % skip_alpha_len]


def solution(s, skip, index):
    alphabet_list = get_skip_alphabet_list(skip)

    shift_s = "".join([
        shift_alphabet(alphabet, index, alphabet_list) for alphabet in list(s)
    ])

    return shift_s