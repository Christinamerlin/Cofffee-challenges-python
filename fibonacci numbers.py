def solution(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return solution(n-1)+solution(n-2)

def main():
    n=int(input())
    print(solution(n))

main()
