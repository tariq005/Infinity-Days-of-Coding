#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, x;
    cin >> x >> n;
    set<int> positions;
    positions.insert(0);
    positions.insert(x);
    multiset<int> lengths;
    lengths.insert(x);

    for (int i = 0; i < n; i++)
    {
        int z;
        cin >> z;
        positions.insert(z);
        auto w = positions.find(z);
        int u = *prev(w);
        int v = *next(w);
        lengths.erase(lengths.find(v-u));
        lengths.insert(z-u);
        lengths.insert(v-z);
        cout << *lengths.rbegin() << " ";
    }
    cout << endl;
    return 0;
}
