#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int N, A, B, C;
	int D[100];

	cin >> N >> A >> B >> C;
	for (int i = 0; i < N; i++) {
		cin >> D[i];
	}
	sort(D, D + N);

	int di = 0;
	double max = (double)C/A;
	for (int i = N - 1; i >= 0; i--) {
		double cpd;
		di += D[i];
		cpd = (double)(C + di) / (A + B * (N - i));
		if (max <= cpd) {
			max = cpd;
		}
		else {
			break;
		}
	}
	printf("%d\n", (int)max);
	

}