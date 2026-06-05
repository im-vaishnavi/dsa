from itertools import permutations 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        all_perms = list(permutations(nums)) 
        all_set = set(all_perms)  
        ans = list(all_set)
        return ans