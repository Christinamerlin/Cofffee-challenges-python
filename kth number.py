#TO find the kth smallest and largest number
def solution(arr,n,k):
    arr.sort()
    print(arr[k-1])
    arr.sort(reverse=True)
    print(arr[k-1])
    
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())

    solution(arr,n,k)

main()

''' 
Input:
5
11 5 12 6 13
2

Output:
6 
12
''' 
