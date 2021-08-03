/*
	esercizio con le condizioni e i cicli
	
	un gruppo di 5 persone(input) ha diritto ad uno sconto
	determinato dall'età della persona più giovane,
*/
#include <iostream>
using namespace std;

int main(){
	int ages[5];
	
	//ciclo per prendere in input le 5 età
	for (int i = 0; i < 5; ++i){
		cin >> ages[i];
	}
	//verifico l'eta minore tra tutte
	if (ages[0] < ages[1]){
		if (ages[0] < ages[2]){
			if (ages[0] < ages[3]){
				if (ages[0] < ages[4]){
					float sconto = 50.0 / 100;
					float sott = 50 - sconto * ages[0];
					cout << sott << endl;
				}
			}
		}
	}
	if (ages[1] < ages[0]){
		if (ages[1] < ages[2]){
			if (ages[1] < ages[3]){
				if (ages[1] < ages[4]){
					float sconto = 50.0 / 100;
					float sott = 50 - sconto * ages[1];
					cout << sott << endl;
				}
			}
		}
	}
	if (ages[2] < ages[1]){
		if (ages[2] < ages[0]){
			if (ages[2] < ages[3]){
				if (ages[2] < ages[4]){
					float sconto = 50.0 / 100;
					float sott = 50 - sconto * ages[2];
					cout << sott << endl;
				}
			}
		}
	}
	if (ages[3] < ages[1]){
		if (ages[3] < ages[2]){
			if (ages[3] < ages[0]){
				if (ages[3] < ages[4]){
					float sconto = 50.0 / 100;
					float sott = 50 - sconto * ages[3];
					cout << sott << endl;
				}
			}
		}
	}					
	if (ages[4] < ages[1]){
		if (ages[4] < ages[2]){
			if (ages[4] < ages[3]){
				if (ages[4] < ages[0]){
					float sconto = 50.0 / 100;
					float sott = 50 - sconto * ages[4];
					cout << sott << endl;
				}
			}
		}
	}
	//operazione di calcolo sconto
	if (ages[0] == ages[1] && ages[1] == ages[2] && ages[2] == ages[3] && ages[3] == ages[4]){
		float sconto = 50.0 / 100;
		float sott = 50 - sconto * ages[0];
		cout << sott << endl;
	}
}

