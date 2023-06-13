'''
Input:
leetcode
Output: 
0
The position of the first non repeating character is 0
'''


def solution(value):
    d={}
    for i in value:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for j,i in enumerate(value):
        if d[i]==1:
            return j
    return -1

def main():
    value = input()
    print(solution(value))
main()
