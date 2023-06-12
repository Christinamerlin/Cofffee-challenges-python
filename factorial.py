''' 
Input:
5
Output:
120
Explanation:
5 * 4 * 3 * 2 * 1 = 120
'''

def solution(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main():
    n=int(input())
    print(solution(n))

main()
