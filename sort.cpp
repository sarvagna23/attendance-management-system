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
    int zero=0,one=0,two=0;
    for(int i=0;i<n;i++){
        if(arr[i]==0){
            zero++;
        }
        else if(arr[i]==1){
            one++;
        }
        else{
            two++;
        }
    }
    for(int i=0;i<zero;i++){
        cout << 0 << " ";
    }
    for(int i=0;i<one;i++){
        cout << 1 << " ";
    }
    for(int i=0;i<two;i++){
        cout << 2 << " ";
    }
    cout << endl;for(int i=0;i<zero;i++){
        cout << 0 << " ";
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        nobody();
    }
}

