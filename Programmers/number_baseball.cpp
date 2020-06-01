#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> baseball) {
	int answer = 0;
	vector<int> pool;
	for (int a = 1; a <= 9; a++) {
		for (int b = 1; b <= 9; b++) {
			for (int c = 1; c <= 9; c++) {
				if (a != b and a != c and b != c) {
					pool.push_back(100 * a + 10 * b + c);
				}
			}
		}
	}

	for (int i = 0; i < pool.size(); i++) {
		string num = to_string(pool[i]);
		for (int j = 0; j < baseball.size(); j++) {
			string guess = to_string(baseball[j][0]);
			int strike = 0; int ball = 0;
			for (int k = 0; k < 3; k++) {
				for (int m = 0; m < 3; m++) {
					if (num[k] == guess[m]) {
						if (k == m) {	//strike
							strike++;
						}
						else {	//ball
							ball++;
						}
					}
				}
			}
			if (j == baseball.size() - 1) {
				if(strike == baseball[j][1] && ball == baseball[j][2]){
					answer++;
				}
			}
			else {
				if (strike != baseball[j][1] || ball != baseball[j][2]) {
					break;
				}
			}
			
			
		}
		
	}

	return answer;
}

int main(void) {
	vector<vector<int>> baseball = { {123,1,1}, {356,1,0}, {327,2,0}, {489,0,1} };
	printf("%d", solution(baseball));
}