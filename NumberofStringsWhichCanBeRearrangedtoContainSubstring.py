class Solution:
    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0
        mod = 1000000007
        ans = pow(26, n, mod)
        rest = pow(25, n, mod)
        rest += pow(25, n, mod)
        rest += pow(25, n, mod)
        rest += (n*pow(25, n-1, mod))%mod
        rest -= pow(24, n, mod)
        rest -= pow(24, n, mod)
        rest -= (n*pow(24, n-1, mod)%mod)
        rest -= pow(24, n, mod)
        rest -= (n*pow(24, n-1, mod)%mod)
        rest += pow(23, n, mod)
        rest += (n*pow(23, n-1, mod))%mod
        return ((ans%mod) - (rest%mod))%mod
