#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	vector<int> st;
	st.assign(n + 2, 1);
	for (int i = 0; i < lost.size(); i++) {
		st[lost[i]]--;
	}
	for (int i = 0; i < reserve.size(); i++) {
		st[reserve[i]]++;
	}
	for (int i = 1; i < n + 1; i++) {
		if (st[i] == 2) {
			if (st[i - 1] == 0) {		//앞만 0 or 앞뒤 0
				st[i - 1]++;
				st[i]--;
				continue;
			}
			if (st[i + 1] == 0) {		//뒤만 0
				st[i + 1]++;
				st[i]--;
			}
		}
	}
	for (int i = 1; i < n + 1; i++) {
		if (st[i] != 0) {
			answer++;
		}
	}

	return answer;
}

int main(void) {
	printf("%d", solution(3, { 3 }, { 1 }));
}