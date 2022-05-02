class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        
        def helper(idx, S):
            SofIdx = mem.get((idx, S))
            
            if SofIdx is not None:
                return SofIdx
            
            if (idx == len(nums)):
                return 1 if S==target else 0
            
            plus = helper(idx+1, S+nums[idx])
            minus = helper(idx+1, S-nums[idx])
            nextS = plus+minus
            mem[(idx, S)] = nextS
            return nextS
        return helper(0,0)
        