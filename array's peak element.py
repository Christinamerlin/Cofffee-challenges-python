'''
Input:
5
1 10 3 9 4

Output:
1
'''
def solution(a, n):
    max=0
    for i,val in enumerate(a):
        if val>max:
            max=val
            index=i
    return index

def main():
    n = int(input())
    a = input().split(" ")
    for i in range(n):
        a[i] = int(a[i])
        
    print(solution(a, n))

main()
