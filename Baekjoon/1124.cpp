#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main() {
	int A, B;
	cin >> A >> B;

	//에라토스테네스 체
	bool prime[100001] = { false, };
	prime[1] = true;
	prime[0] = true;
	int arr[100001] = { 0 };
	int count = 0;

	for (int i = 2; i <= 100000; i++) {
		if (prime[i] == false) {
			// i의 배수 지우기
			for (int j = i + i; j <= B; j += i) {
				prime[j] = true;
				int x = j;
				while (x%i == 0) {
					x /= i;
					arr[j]++;
				}
			}
		}
	}
	for (int i = A; i <= B; i++) {
		if (prime[arr[i]] == false) count++;
	}

	printf("%d", count);
}