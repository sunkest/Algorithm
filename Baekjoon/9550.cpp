#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	vector<int> ans;
	for (int i = 0; i < T; i++) {
		int n, k;
		cin >> n >> k;
		int a = 0;
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			a += (x / k);
		}
		ans.push_back(a);
	}
	for (int i = 0; i < T; i++) {
		printf("%d\n", ans[i]);
	}

}