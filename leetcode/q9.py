class Solution:
    
    def __init__(self, x,):     
        self.x = x
        
    def isPalindrome(self, x):
        if x < 0:
            print(False)
            return(False)
        print(str(x) == str(x)[::-1])


x = 121
answer = Solution(x)
answer.isPalindrome(x)
            