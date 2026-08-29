class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        setnum = set(nums)

        longest = 0

        for i in nums :
            

            if i-1 in setnum :
                continue
            else :
                c=0

                c+=1
                num = i +1
                
                while num in setnum :
                    c+=1
                    num+=1

                longest = max(c, longest)

        

        return longest

                


            
        