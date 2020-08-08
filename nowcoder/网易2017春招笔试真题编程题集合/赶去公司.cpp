#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>

using namespace std;

int main() {
    int n;
    cin>>n;
    int x[n], y[n];
    for(int i=0;i<n;++i){
        cin>>x[i];
    }
    for(int i=0;i<n;++i){
        cin>>y[i];
    }
    int gx, gy, walk, taxi;
    cin>>gx>>gy>>walk>>taxi;
    int res = (abs(gx) + abs(gy)) * walk;
    for(int i=0;i<n;++i){
        long long tmp = (abs(x[i]) + abs(y[i])) * walk;
        tmp = tmp + (abs(gx - x[i]) + abs(gy - y[i])) * taxi;
        if (tmp < res)res=tmp;
    }
    cout<<res<<endl;
    return 0;
}