'''
Input:
18
Output:
2
Explanation:
The binary representation of 18 is 010010,the first set bit from the right side is at position 2. 32 bit integer  is considered for conversion.
'''

def solution(n):
    b=format(n,'032b')
    rev=b[::-1]
    for i,bit in enumerate(rev):
        if bit=='1':
            return i+1
    return -1

def main():
    n=int(input())
    print(solution(n))

main()
