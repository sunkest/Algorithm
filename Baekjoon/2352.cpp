#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	int n;
	vector<int> v;
	vector<int> lis;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		v.push_back(x);
	}

	lis.push_back(v[0]);
	for (int i = 1; i < n; i++) {
		if (v[i] > lis[lis.size() - 1]) {
			lis.push_back(v[i]);
		}
		else {
			int x = lower_bound(lis.begin(), lis.end(), v[i]) - lis.begin();
			lis[x] = v[i];
		}
	}

	printf("%d\n", lis.size());

}