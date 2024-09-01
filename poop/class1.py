class Solution:
    
    def __init__(self, nums):     
        self.nums = nums
        
          
    def runningSum(self, nums):
        x = 0
        lst = []
        for number in nums:
            x = number + x
            lst.append(x)
        print(lst)
        return(lst)





# the following lines of code are how to get the input and output
nums = [1,3,4,5,6]
answer = Solution(nums)
answer.runningSum(nums)
#output is 1 + 0 = [1] x remains = 1
#output is 3 + 1 = [1,4] x remains = 4


# this problem is leetcode 1480 and this is how it is solved on vscode 
# however leetcode already has the init and does not need that it only needs the function 
# in leetcode you need a return or it wont work even tho if i want to see it i need to print it so I did both to make more sense to me.