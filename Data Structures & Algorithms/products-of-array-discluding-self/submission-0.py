class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0 for i in range(len(nums))]
        postfix = [0 for i in range(len(nums))]

        for i in range(len(nums)) :
            if i == 0 :
                prefix[i] = nums[i]

            else :
                prefix[i] = prefix[i-1] * nums[i]
            
        for i in range(len(nums)-1,-1,-1) :
            if i == len(nums)-1 :
                postfix[i] = nums[i]

            else :
                postfix[i] = postfix[i+1] * nums[i]

        output = [0 for i in range(len(nums))]

        for i in range(len(nums)) :
            if i == 0 :
                output[i] = postfix[i+1]

            elif i == len(nums)-1 :
                output[i] = prefix[i-1]

            else :
                output[i] = prefix[i-1] * postfix[i+1]

        return output

            

        