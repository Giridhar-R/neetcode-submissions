class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)-2) :

            if nums[i]==nums[i-1] and i>0 :
                continue

            low = i+1
            high = len(nums)-1

            while low< high :
                if nums[i] +nums[low]+nums[high] >0:
                    high-=1

                elif nums[i] +nums[low]+nums[high] <0:
                    low +=1

                else :
                    res.append([nums[i], nums[low], nums[high]])

                    low+=1
                    
                    while nums[low-1]==nums[low] and low< high:
                        low +=1

        return res




                




        