class Solution:
    
    def __init__(self, nums, target):     
        self.nums = nums
        self.target = target
        
          
    def runningSum(self, nums, target):
        x = 0
        a = nums.index(x)
        b = nums.index(number)
        lst = [a,b]
        new_lst = []
        for number in nums:
            if x + number == target:
                print(new_lst.extend(lst))
            else:
                x += number 
            
            

       





# the following lines of code are how to get the input and output
nums = [2,7,11,15]
target = 9
answer = Solution(nums, target)
answer.runningSum(nums, target)
#output is 1 + 0 = [1] x remains = 1
#output is 3 + 1 = [1,4] x remains = 4

