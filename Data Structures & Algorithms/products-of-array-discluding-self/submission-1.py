class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        output = [0 for i in range(len(nums))]
        pre = 1

        for i in range(len(nums)) :
            output[i] = pre 
            pre *= nums[i]

        pre = 1
        for i in range(len(nums)-1,-1,-1) :
            output[i] = pre * output[i]
            pre *= nums[i]

        return output

            

        