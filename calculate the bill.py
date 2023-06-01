def solution(h, n, k, b):
    del h[k]
    f=0
    f=int(sum(h)/2)
    if(b>f):
        print(b-f)
    else:
        print("Bon Appetit")
        
def main():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    a = input().split(" ")
    for i in range(n):
        a[i] = int(a[i])
    b = int(input())
    solution(a, n, k, b)
    
main()
