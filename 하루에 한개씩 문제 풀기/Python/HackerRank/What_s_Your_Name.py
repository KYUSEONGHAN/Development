# HackerRank, What's Your Name?, python3
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')


if __name__ == '__main__':
    firstname = str(input())
    lastname = str(input())

    print_full_name(firstname, lastname)