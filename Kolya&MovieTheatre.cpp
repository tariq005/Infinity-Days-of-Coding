#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long long n, m, d;
        cin >> n >> m >> d;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
        long long ans = 0, sum = 0;
        multiset<long long> s;
        for (int i = 0; i < n; i++)
        {
            long long cur = sum + a[i] - d*(i+1);
            ans = max(ans, cur);
            if (a[i] > 0)
            {
                s.insert(a[i]);
                sum += a[i];
                if (s.size() >= m)
                {
                    sum -= *s.begin();
                    s.erase(s.begin());
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}
