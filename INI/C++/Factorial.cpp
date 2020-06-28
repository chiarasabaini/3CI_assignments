#include <iostream>
using namespace std;

//funzione ricorsiva che stampa il fattoriale di un numero
//se in 32 bit va in overflow
unsigned long long factorial(int n){
	if (n==1){
		return 1;
	}
	else {
        unsigned long long res = n*factorial(n-1);
        cout << n << "\t" << res << endl;
	    return res;
	}
}
int main(){
    int f;
    cout << LONG_LONG_MAX << endl;
    cin>>f;
    cout<<f<<endl;
    unsigned long long res = factorial(f);
	cout<< res;
}
