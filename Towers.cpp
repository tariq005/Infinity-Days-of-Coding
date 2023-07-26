#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> cube(n);
    for (int i = 0; i < n; i++)
        cin >> cube[i];

    multiset<int> towers;
    for (int i = 0; i < n; i++)
    {
        if (towers.size() == 0)
            towers.insert(cube[i]);
        else
        {
            auto x = towers.upper_bound(cube[i]);
            if (x == towers.end())
                towers.insert(cube[i]);
            else
            {
                towers.insert(cube[i]);
                towers.erase(x);
            }
        }
    }
    cout << towers.size() << endl;
    return 0;
}
