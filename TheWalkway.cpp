#include <bits/stdc++.h>
using namespace std;

int find(int lo, int hi, int d) {
    return (hi - lo - 1) / d;
}

void solve() {

    int n, m, d;
    cin >> n >> m >> d;

    vector<int> a(m);
    for (int i = 0; i < m; i++)
    {
        int x;
        cin >> x;
        a[i] = x;
    }

    vector<int> pre(m), suff(m);

    pre[0] = 1 + (a[0] + d - 2) / d;
    for(int i = 1; i < m; i++) {
        pre[i] = 1 + pre[i - 1] + find(a[i - 1], a[i], d);
    }

    suff[m - 1] = 1 + find(a[m - 1], n + 1, d);

    for(int i = m - 2; i >= 0; i--) {
        suff[i] = 1 + suff[i + 1] + find(a[i], a[i + 1], d);
    }

    map<int,int> mp;

    int ans = (a[1] + d - 2) / d + suff[1];
    mp[ans]++;

    for(int i = 1; i < m - 1; i++) {
        int curr = pre[i - 1] + suff[i + 1] + find(a[i - 1], a[i + 1], d);
        if(curr < ans) {
            ans = curr;
        }
            mp[curr]++;
    }

    {
        int curr = pre[m - 2] + find(a[m - 2], n + 1, d);
        if(ans > curr) {
            ans = curr;
        }
            mp[curr]++;
    }

    cout << ans << " " << mp[ans] << endl;

}

int main() {

    int t = 1;
    cin >> t;

    while(t--) {
        solve();
    }

    return 0;
}
