#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

int main(void) {
	vector<pair<int, int>> v;
	int n;
	cin >> n;
	v.resize(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i].second >> v[i].first;
	}
	sort(v.begin(), v.end());

	int sum = 0;
	bool sc[1001] = { 0 };
	for (int i = v.size() - 1; i >= 0; i--) {
		int x = v[i].second;
		while (x >= 1) {
			if (sc[x] == 0) {
				sc[x] = true;
				sum += v[i].first;
				break;
			}
			x--;
		}
	}
	printf("%d\n", sum);
}