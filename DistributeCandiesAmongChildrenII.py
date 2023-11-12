class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n/3 > limit:
            return 0
        ans = 0
        for i in range(min(limit, n)+1):
            if (n-i)/2 > limit:
                continue
            m = n-i
            ans += max(min(m, limit)-max(m-limit, 0)+1, 0)
        return ans
