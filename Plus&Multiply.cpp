#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, a, b, t;
    cin >> t;
    while (t--)
    {
        cin >> n >> a >> b;
        if (n == 1 || b == 1 || n%b == 1)
            cout << "YES" << endl;
        else if (a == 1)
            if (n%b == 1)
            {
                cout << "YES" << endl;
            }
            else
                cout << "NO" << endl;
        else
            {
                int x = 0, ans = 0;
                long long z;
                while (pow(a, x) <= n)
                {
                    z = n-pow(a, x);
                    if (z%b == 0)
                    {
                        ans = 1;
                        break;
                    }
                    x++;
                }

            if (ans == 1)
                {
                    cout << "YES" << endl;
                }
            else
                cout << "NO" << endl;
            }
    }
}
