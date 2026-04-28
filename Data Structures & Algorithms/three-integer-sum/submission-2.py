class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        for i, select in enumerate(nums):
            if select > 0:
                break
            
            if i>0 and select == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = select + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([select, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums [l-1] and l<r:
                        l+=1
        return res