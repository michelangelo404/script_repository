#include <iostream>
using namespace std;

int main() {
	 int a;
	 int b = 2;
	 int c = 1;
	 while (c < 999){
		a = b + c;
		cout << a << endl;
		c = b + a;
		cout << c << endl;
		b = c + a;
		cout << b << endl;
	 }
}
	 
