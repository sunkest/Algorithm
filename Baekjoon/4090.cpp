#include <iostream>
using namespace std;
int Vampire(int n);

int main(void) {
	int n;
	cin >> n;
	while (!Vampire(n)) { n++; }
	cout << n << endl;

	return 0;
}

int Vampire(int n) {
	int A[10] = {};
	int B[10] = {};

	for (int i = n; i > 0; i /= 10) {
		A[i % 10]++;
	}
	for (int m = 1; m*m <= n; m++) {
		if (n % m) 	continue;
		int p = m;
		int q = n / m;
		for(int j = 0; j < 10; j++) {
			B[j] = 0;
		}
		for (int r = p; r > 0; r /= 10) {
			B[r % 10]++;
		}
		for (int s = q; s > 0; s /= 10) {
			B[s % 10]++;
		}

		for (int k = 0; k < 10; k++) {
			if (A[k] != B[k]) {
				break;
			}
			if (k == 9) {
				return 1;
			}
		}
	}
	return 0;
}