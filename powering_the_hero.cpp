#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while (t--)
    {
        int n;
        cin>>n;
        vector<long long> a(n);
        for (int i=0; i<n; i++)
        {
            cin>>a[i];
        }
        long long ans= 0;
        priority_queue<long long> pq;
        for (int i= 0; i<n; i++)
        {
            if (a[i] == 0)
            {
                if (pq.empty())
                    continue;
                ans += pq.top();
                pq.pop();
            }
            else
            {
                pq.push(a[i]);
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
