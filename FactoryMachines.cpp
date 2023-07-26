#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, t;
    cin >> n >> t;
    vector<int> machines(n);
    for (int i = 0; i < n; i++)
        cin >> machines[i];

    long long low = 0, high = 1e18, ans = 1e18;
    while (low <= high)
    {
        long long mid = (low+high)/2;
        long long products = 0;
        for (int i = 0; i < n; i ++)
            products += min(mid/machines[i], (long long)1e9);

        if (products >= t)
        {
            ans = min(ans, mid);
            high = mid-1;
        }
        else
            low = mid+1;
    }
    cout << ans << endl;
}
