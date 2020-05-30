#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int C;
	cin >> C;
	
	vector<string> S;
	vector<string> T;
	vector<int> ans;
	S.resize(C);
	T.resize(C);
	ans.resize(C);

	for (int i = 0; i < C; i++) {
		cin >> S[i] >> T[i];
		ans[i] = 0;
	}

	for (int i = 0; i < C; i++) {
		int a = 0, b = 0, c = 0, d = 0;
		for (int j = 0; j < S[i].length(); j++) {
			if(T[i][j] == '0'){
				if (S[i][j] == '1') b++;
				else if (S[i][j] == '?') c++;
			}
			else if (T[i][j] == '1') {
				if (S[i][j] == '0') a++;
				else if (S[i][j] == '?') d++;
			}
		}
		ans[i] += min(a, b);
		if (a - b >= 0) {
			ans[i] += a - b;	  //남은0->1
			ans[i] += c + d; //?를 T대로 바꾸기
		}
		else if (a - b < 0) {
			if (b > d) {
				ans[i] = -1;		//불가능
				continue;
			}
			else {	//남은1은 ?에서 땡겨오고 자리바꿈
				ans[i] += b - a;
				ans[i] += c + d;
			}
		}
	}

	for (int i = 0; i < C; i++) {
		printf("Case %d: %d\n", i+1, ans[i]);
	}




}