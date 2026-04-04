class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            # If count is zero, we pick a new potential candidate
            if count == 0:
                candidate = num
            
            # If current number matches candidate, increment; else decrement
            count += (1 if num == candidate else -1)

        return candidate
            
        

            

