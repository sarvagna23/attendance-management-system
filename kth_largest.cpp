#include <bits/stdc++.h>
using namespace std;
#define ll long long 

void nobody(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    int k;
    cin >> k;
    priority_queue<int,vector<int>,greater<int>> p;
    for(int i=0;i<n;i++){
        p.push(arr[i]);
    }
    int ans;
    for(int i=0;i<n;i++){
        if(i+1==k){
            ans=p.top();
        }
        p.pop();
    }
    cout << ans << endl;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        nobody();
    }
}
