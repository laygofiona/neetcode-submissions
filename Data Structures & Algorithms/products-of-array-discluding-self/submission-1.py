class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        for num in nums:
            new_nums = [*nums]
            new_nums.remove(num)
            product = 1
            for new_num in new_nums:
                product *= new_num
            results.append(product)
        
        return results
        