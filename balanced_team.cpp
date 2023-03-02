#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<int> a(n);
    for (int i=0; i<n; i++)
        cin>>a[i];
    sort(a.begin(), a.end());
    int j= 0;
    int maxx= 0;
    for (int i=0; i<n; i++)
    {
        while ((j<n) && ((a[j]-a[i]) <= 5))
        {
            j++;
            maxx= max(j-i, maxx);
        }
    }
    cout << maxx << endl;
    return 0;
}
