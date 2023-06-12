'''
Input:
abcd
Output:
dcba

NOTE:
Built-in functions must not be used.
'''
def solution(str):
   s=str[::-1]
   return s


def main():
    str = input()
    ans = solution(str)
    print(ans)
    
main()
