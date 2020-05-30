#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> v;
	for (; n != 0; n /= 10) {
		v.push_back(n % 10);
	}
	reverse(v.begin(), v.end());
	bool flag = false;
	for (int i = v.size() - 1; i >=1; i--) {
		if (v[i - 1] < v[i]) {
			for (int j = v.size() - 1; j >= i; j--) {
				if (v[j] > v[i-1]) {
					int temp = v[i-1];
					v[i-1] = v[j];
					v[j] = temp;
					reverse(v.begin() + i , v.end());
					flag = true;
					break;
				}
			}
		}
		if (flag) break;
	}
	if (flag) {
		for (int i = 0; i < v.size(); i++) {
			printf("%d", v[i]);
		}
	}
	else {
		printf("0");
	}

	
	

}