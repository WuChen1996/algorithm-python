class Solution:
    def smallestRangeI(self, lst, k: int) -> int:
        min_ = min(lst)
        max_ = max(lst)
        if max_ - min_ - 2*k > 0:
            return max_ - min_ - 2*k
        else:
            return 0
        
s = Solution()
s.smallestRangeI([1,3,10],3)