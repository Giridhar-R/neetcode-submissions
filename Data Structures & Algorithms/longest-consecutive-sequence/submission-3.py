class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 :
            return 0

        setnum = set(nums)

        seq = []

        for i in nums :
            

            if i-1 in setnum :
                continue
            else :
                c=[]

                c.append(i)
                num = i +1
                
                while num in setnum :
                    c.append(num)
                    num+=1

                seq.append(len(c))

        if len(seq)==0 :
            seq.append(1)

        return max(seq)

                


            
        