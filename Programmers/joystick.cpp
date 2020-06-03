#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(string name) {
	int answer = 0;
	int count_A = 0;
	int cur = 0;
	for (int i = 0; i < name.size(); i++) {
		if (name[i] == 'A') count_A++;
	}
	for (int i = 0;; i++) {
		answer += min(name[cur] - 'A', 'Z' - name[cur] + 1);
		printf("%d added from up/down\n", min(name[cur] - 'A', 'Z' - name[cur] + 1));
		name[cur] = 'A';
		cout << name << endl;
		bool flag = true;
		for (int j = 0; j < name.size(); j++) {
			if (name[j] != 'A') {
				flag = false;
				break;
			}
		}
		if (flag) break;

		int left = 0, right = 0;
		for (int j = 1; j < name.size(); j++) {
			if (name[(cur + j)%name.size()] == 'A') {
				right++;
			}
			else break;
		}
		for (int j = 1; j < name.size(); j++) {
			int index = cur - j;
			if (cur - j < 0) index += name.size();
			if (name[(index)] == 'A') {
				left++;
			}
			else break;
		}

		if (right <= left) {
			cur += right + 1;
			cur %= name.size();
			answer += right + 1;
			printf("%d added from right\n", right + 1);
		}
		else {
			cur -= left + 1;
			if (cur < 0) cur += name.size();
			answer += left + 1;
			printf("%d added from left\n", left + 1);

		}
		
	}
	return answer;
}

int main(void) {
	printf("%d", solution("CANAAAAANAN"));
}