#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int n= s.length();
    int flag= 0;
    for (int i= 0; i<n; i++)
    {
        if (s[i] != 'a')
        {
            s[i]--;
            flag= 1;
        }
        else
        {
            if (flag == 1)
            {
                break;
            }
        }
    }

    if (flag == 0)
    {
        s.back()= 'z';
    }
    cout << s << endl;
    return 0;
}
