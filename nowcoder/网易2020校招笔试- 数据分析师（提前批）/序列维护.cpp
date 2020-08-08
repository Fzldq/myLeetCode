#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main() {
    int n, q;
    cin>>n>>q;
    int nlst[n];
    for (int i=0; i<n; ++i) {
        cin>>nlst[i];
    }
    sort(nlst, nlst+n);
    int tmp, res;
    while(q--){
        cin>>tmp;
        res = 0;
        for (int i=n-1; i>=0; --i){
            if(nlst[i] >= tmp){
                res++;
                nlst[i]--;
            }
            else break;
        }
        cout << res << endl;
    }
    return 0;
}