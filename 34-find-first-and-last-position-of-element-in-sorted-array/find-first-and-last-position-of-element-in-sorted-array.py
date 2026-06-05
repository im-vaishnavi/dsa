class Solution:
    def upperbound(self,nums,target):
        ans=len(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>target:
                ans=mid
                r=mid-1
            else:
                l=mid+1
                
        return ans
    def lowerbound(self,nums,target):
        ans=len(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l=mid+1
                
            else:
                r=mid-1
                ans=mid
                
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.lowerbound(nums,target)
        b=self.upperbound(nums,target)
        if a==b:
            return [-1,-1]
        else:
            return [a,b-1]
