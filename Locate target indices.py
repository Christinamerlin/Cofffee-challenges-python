def solution(h, n, k):
    flag=False
    h.sort()
    for i in range(len(h)):
        if h[i]==k:
            print(i,end=' ')
            flag=True
    if not flag:
        print("-1")
def main():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    a = input().split(" ")
    for i in range(n):
        a[i] = int(a[i])
    
    solution(a, n, k)
    
main()
