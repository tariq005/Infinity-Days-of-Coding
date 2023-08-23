#include <bits/stdc++.h>
using namespace std;
int mx = 15000005;
int gcd(int a, int b)
{
    return ((b==0)?a:gcd(b,a%b));
}

int main()
{
    vector<int> lp(mx+1, 1);
    lp[0] = lp[1] = 1;
    for (int i = 2; i < mx+1; i++)
        if (lp[i] == 1)
            for (int j = i; j < mx+1; j += i)
                lp[j] = i;

    int n, g = 0;
    cin >> n;
    vector<int> num(n);
    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
        g = gcd(g, num[i]);
    }

    for (int i = 0; i < n; i++)
        num[i] /= g;
    map<int, int> mp;
    for (int i = 0; i < n; i++)
    {
        while (num[i] != 1)
        {
            int l = lp[num[i]];
            mp[l]++;
            while (num[i] % l == 0)
                num[i] /= l;
        }
    }

    int ans = n;
    for (auto x: mp)
        ans = min(ans, n-x.second);
    if (ans == n)
        cout << -1 << endl;
    else
        cout << ans << endl;
    return 0;
}
