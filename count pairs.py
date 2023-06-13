'''
Input:
5 2
1 5 3 4 2
Output:
3
'''
def solution(h, n, k):
   cnt=0
   d={}
   for i in h:
       if i+k in d:
           cnt+=d[i+k]
       if i-k in d:
            cnt+=d[i-k]
       d[i]=d.get(i,0)+1
   return cnt
            

def main():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    a = input().split(" ")
    for i in range(n):
        a[i] = int(a[i])
    print(solution(a, n, k))

main()   
