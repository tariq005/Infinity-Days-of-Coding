#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, t, N= 1e4+2, a[N];
    cin>>t;
    while (t--)
    {
        cin>>n;
        for (int i=1; i<=n; i++)
            cin>>a[i];

        if (a[1] == 1)
        {
            cout<<n+1<< ' ';
            for (int i=1; i<=n; i++)
                cout<<i<< ' ';
            cout<<endl;
        }
        else if (a[n] == 0)
        {
            for (int i=1; i<=n; i++)
                cout<<i<< ' ';
            cout<<n+1<< ' ';
            cout<<endl;
        }
        else
        {
            int p= 0;
            for (int i=1; i<=n; i++)
            {
                cout<<i<< ' ';
                if (a[i] == 0 && a[i+1] == 1 && !p)
                {
                    cout<<n+1<< ' ';
                    p ++;
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
