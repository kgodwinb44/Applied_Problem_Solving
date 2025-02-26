# Majority Element II

class Solution(object):
    def majorityElement(self, nums):
        
        counts = {}  
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
         
        result = []
        for num, count in counts.items():
            if count > len(nums)/3:
                result.append(num)
        return result

nums = [3,2,3,2,6,6,6,6,9]
sol = Solution()
print(sol.majorityElement(nums))


    