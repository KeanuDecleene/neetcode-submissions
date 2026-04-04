class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_dict = {}

        for num in nums:
            if num in number_dict:
                pass
            number_dict[num] = nums.count(num)
        
        res = max(number_dict, key=number_dict.get)    

        return res       
        
        
        

            

