#include<iostream>
#include<algorithm>
#include <vector>
using namespace std;
int LIS(int m);
int LDS(int m);

vector<int> v;
vector<int> lis;
int N;

int main(void) {

	cin >> N;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		v.push_back(x);
	}
	int max = 0;
	for (int i = 0; i < N-1; i++) {
		int s = LIS(i) + LDS(i) - 1;
		if (s > max) max = s;
	}

	printf("%d\n", max);
}

int LIS(int m) {
	lis.clear();
	lis.push_back(v[m]);
	for (int i = m+1; i < N; i++) {
		if (v[i] > lis[lis.size() - 1]) {
			lis.push_back(v[i]);
		}
		else {
			int x = lower_bound(lis.begin(), lis.end(), v[i]) - lis.begin();
			lis[x] = v[i];
		}
	}
	return lis.size();
}

int LDS(int m) {
	lis.clear();
	lis.push_back(v[m]);
	for (int i = m+1; i < N; i++) {
		if (v[i] < lis[lis.size() - 1]) {
			lis.push_back(v[i]);
		}
		else {
			int x = upper_bound(lis.begin(), lis.end(), v[i]) - lis.begin() -1;
			lis[x] = v[i];
		}
	}
	return lis.size();
}