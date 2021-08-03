//esercizio preso da video https://youtu.be/2bkfA2fHVwg
#include <iostream>
using namespace std;

int main(){
	int f; //vigili del fuoco
	int p; //polizia
	int s; //sanità
	for (f = 2; f < 10; f += 2){
//		cout << "1x" << f << p << s << endl;
		for (p = 1; p <= 10; p++){
//			cout << "2x" << f << p << s << endl;
			for (s = 1; s <= 10; s++){
//				cout << "3x" << f << p << s << endl;
				if (f != p && p != s && s != f && f + p + s == 12){
					cout << f << " " << p << " " << s << endl;
				}
			}
		}
	}
}
/* con i for annidati vengono inizializzati i primi for, successivamente
il programma esegue le iterazioni nell'ultimo for, appena la condizione risulta falsa 
il programma passa al secondo for, NON RINIZIA DAL PRIMO, poichè il terzo è annidato nel
secondo. Passanso al secondo for il ragionamento si ripete. Per capire meglio
disattivare commenti sui cout. */
