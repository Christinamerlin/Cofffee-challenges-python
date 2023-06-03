def solution(a, n):
    for i in a:
        print(a.count(i))

def main():
    n = int(input())
    a = input().split(" ")
    for i in range(n):
        a[i] = int(a[i])
    solution(a, n)

main()
'''
Input:
5
2 2 4 6 6
Output:
4
'''
