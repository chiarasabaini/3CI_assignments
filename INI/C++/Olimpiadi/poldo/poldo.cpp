#include <iostream>
#include <stdio.h>
#include <assert.h>
#include <bits/stdc++.h>
using namespace std;

int main(){
    //uncomment the following lines if you want to read/write from files
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}
int mangia(int N, vector<int> p){
    vector<int> panM(N,0);
    int i;
    int mag;
    int magtot=0;
    panM[N-1]=1;
    for(i=N-2; i>=0; i--){
        mag=0;
        for(int k=i+1; k<N; k+1){
            if(p[k]<p[i]){
                if(panM[k]>mag)
                    mag=panM[k];
            }
            panM[i]=mag+1;
            magtot=max(magtot, panM[i]);
        }
    return magtot;
    }
    cout<<magtot;
}
