class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # approach by aditya verma sir and code story with mik
        def solve(nums , output, i, result ):
            # bc 
            if i>=len(nums):
                result.append(output[:])
                return

            # pick case
            output.append(nums[i])
            #call recur for next step 
            solve(nums , output, i+1, result)
            #not  pick case
            output.pop()
            #call recur for next step 
            solve(nums , output, i+1, result)

        result = []
        solve(nums , [], 0, result )
        return result