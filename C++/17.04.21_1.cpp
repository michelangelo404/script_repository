//programma che verifica se un numero e primo o no
#include <iostream>
using namespace std;

int main(){
	int n1;
	int i = 2;
	int resto;
	cout << "inserisci un numero da verificare: " << endl;
	cin >> n1;
	for (n1 = n1; i<n1; ++i){
		resto = n1 % i;
		if (resto == 0){
			cout << n1 << " non è un numero primo";
		}
		if (resto == 1 ){
			cout << n1 << " è un numero primo";
		break;
		}
	}
}


