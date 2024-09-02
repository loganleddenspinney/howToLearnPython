class Solution:
    
    def __init__(self, nums, target):     
        self.nums = nums
        self.target = target
        
          
    def runningSum(self, nums, target):
        n = len(nums)
        lst1 = []
        lst2 = []
        for i in range(n-1):
            lst1.append(i)
            for j in range(i+1, n):
                lst2.append(j)
                if nums[i] + nums[j] == target:
                    print([i,j])
                    return[i,j]
        

        return[]
        
nums = [11,2,15,7]
target = 9
answer = Solution(nums, target)
answer.runningSum(nums, target)
            
            

            
'''            
     def runningSum(self, nums, target):
        n = len(nums)
        lst1 = []
        lst2 = []
        for i in range(n-1):
            lst1.append(i)
            for j in range(i+1, n):
                lst2.append(j)
                
        print(lst1)
        print(lst2)
        

        return[]'''