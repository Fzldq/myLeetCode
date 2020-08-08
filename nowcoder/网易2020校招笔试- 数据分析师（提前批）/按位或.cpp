#include <iostream>
#include <vector>

using namespace std;

bool isexist(vector<int> temp,int x)
{
    int y = 0;
    for (int i = 0; i < temp.size(); i++)
    {
        if ((x | temp[i]) == x)
            y = y | temp[i];
            if (x == y)
                return true;
    }
    return x == y;
}

int main()
{
    int n;
    cin >> n;
    vector<int> temp;
    while (n--)
    {
        int a, x;
        cin >> a >> x;
        if (a == 1)
            temp.push_back(x);
        else
        {
            if (isexist(temp, x))
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }  
    }
    return 0;
}
