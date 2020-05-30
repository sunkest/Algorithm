#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int n;
	cin >> n;
	int *w = new int[n]; //와인 양
	int *d = new int[n]; //n번째까지의 최대
	for (int i = 0; i<n; i++) {
		cin >> w[i];
	}

	//d[n]은 d[n-3]+w[n-1]+w[n], d[n-2]+w[n], d[n-1] 중 최대
	//d[0] = w[0] //d[1] = w[0]+w[1] //d[2] = 세개중에 젤작은거뺀거

	d[0] = w[0];
	d[1] = w[0] + w[1];
	d[2] = w[0] + w[1] + w[2] - min(min(w[0], w[1]), w[2]);

	for (int i = 3; i<n; i++) {
		int m = max(d[i - 1], d[i - 2] + w[i]);
		d[i] = max(m, d[i - 3] + w[i - 1] + w[i]);
	}
	printf("%d\n", d[n - 1]);
}