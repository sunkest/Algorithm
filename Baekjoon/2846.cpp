#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int* arr;
	int n;
	cin >> n;
	arr = new int[n+1];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	arr[n] = 0;

	int max = 0;
	int up = 0;
	for (int i = 1; i < n+1; i++) {
		if (arr[i - 1] < arr[i]) {
			up += arr[i] - arr[i - 1];
		}
		else {
			if (up > max) max = up;
			up = 0;
		}
	}
	printf("%d", max);
}