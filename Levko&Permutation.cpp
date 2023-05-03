#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    if (n == k)
        cout << -1 << endl;
    else if (k == n-1)
    {
        for (int i=0; i<n; i++)
            cout << i+1 << ' ';
        cout << endl;
    }
    else
    {
        int z= 2;
        cout << n << ' ';
        for (int i=0; i<k; i++)
        {
            cout << z << ' ';
            z++;
        }
        cout << 1 << ' ';
        for (int i=0; i<n-k-2; i++)
        {
            cout << z << ' ';
            z++;
        }
        cout << endl;
    }
    return 0;
}
