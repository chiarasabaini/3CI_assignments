#include <iostream>
using namespace std;

int main(){
    //  uncomment the following lines if you want to read/write from files
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int G;
    int P;
    cin>>G>>P;
    int gt=0;
    int t=1;
    while (G>0){
        if(G>=t)
            gt+=t;
        else
            gt+=G;
        G-=t;
        G=G-P+1;
        t++;
    }
    cout<<gt<<endl;
}
