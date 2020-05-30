#include <iostream>
using namespace std;
#define MAX 1000000+1
void primeNum(bool *p);
void Goldbach(int n, bool *p);


int main(void) {
	bool pnum[MAX] = {};
	int n;
	cin >> n;
	primeNum(pnum);

	Goldbach(n, pnum);

	return 0;
}

void Goldbach(int n, bool *p) {
	for (int i = 3; i < n; i++) {
		if (!p[i] && !p[n - i]) {
			cout << n << " = " << i << " + " << n - i << endl;
			return;
		}
	}
	cout << "Goldbach's conjecture is wrong." << endl;
}

void primeNum(bool *p) {
	p[1] = 1;	//소수면 0, 아니면 1
	for (int i = 2; i*i < MAX; i++) {
		if (!p[i]) {
			for (int j = i * i; j < MAX; j += i) {
				p[j] = 1;
			}
		}
	}
}