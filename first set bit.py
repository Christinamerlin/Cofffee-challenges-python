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
