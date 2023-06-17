'''
Input 1:
1
Output 1: 
0
Input 2:
2
Input 2:
1
Input 3:
5
Input 3:
3
'''
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
