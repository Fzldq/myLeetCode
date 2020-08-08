#include <map>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
 
using namespace std;
int main() {
    int n, i, temp, left, right;
    scanf("%d", &n);
    vector<int> a;
    map<int, int> radius;
    map<int, int>::iterator key;
    for (i = 0; i < n; ++i) {
        scanf("%d", &temp);
        a.push_back(temp);
    }
    for (i = 0; i < n; ++i) {
        left = i - 1;
        right = i + 1;
        while (left > -1) {
            if (a[left] > a[i]) {
                break;
            }
            --left;
        }
        while (right < n) {
            if (a[right] > a[i]) {
                break;
            }
            ++right;
        }
        int sum = right - left - 1;
        key = radius.find(sum);
        if (key == radius.end()) {
            radius[sum] = a[i];
        } else {
            if (radius[sum] > a[i]) radius[sum] = a[i];
        }
    }
    int min = radius[n];
    map<int, int>::reverse_iterator rkey;
    for (rkey = radius.rbegin(); rkey != radius.rend(); rkey++) {
        if (min < rkey->second) {
            rkey->second = min;
        } else {
            min = rkey->second;
        }
    }
    int rRes = 1;
    for (i = 1; i <= n; ++i) {
        key = radius.find(rRes);
        if (key == radius.end()) {
            while (key==radius.end()) {
                ++rRes;
                key = radius.find(rRes);
            }
            printf("%d ", key->second);
        } else {
            printf("%d ", key->second);
            if (rRes == i) {
                ++rRes;
            }
        }
    }
    return 0;
}