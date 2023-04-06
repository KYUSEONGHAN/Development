# https://www.acmicpc.net/problem/27889
# boj, 27889: 특별한 학교 이름, python3
def solve(school_name: str) -> str:
    school_dict = {
        'NLCS': 'North London Collegiate School',
        'BHA': 'Branksome Hall Asia',
        'KIS': 'Korea International School',
        'SJA': 'St. Johnsbury Academy'
    }
    return school_dict[school_name]

if __name__ == '__main__':
    school_name = str(input())

    print(solve(school_name))