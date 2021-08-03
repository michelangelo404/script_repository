#include <iostream>
using namespace std; //da mettere sempre perchè altrimenti il codice cambia

int main()
{
	int a = 10;
	cout << a << endl;
	cout << ++a << endl;
	cout << a << endl;
	cout << "primo reset valore di a..." << endl;
	a = 10;
	cout << a << endl;
	cout << a++ << endl;
	cout << a << endl;
}
//senza "using namespace std;" diventerebbe std::cout
