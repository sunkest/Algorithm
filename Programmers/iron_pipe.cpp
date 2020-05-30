#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(string arrangement) {
	int answer = 0;
	stack<char> stk;
	char prev;
	for (int i = 0; i < arrangement.size(); i++) {
		if (arrangement[i] == '(') {
			stk.push('(');
			prev = '(';
		}
		else {
			stk.pop();
			if (prev == '(') { //Laser
				answer += stk.size();
			}
			else {
				answer++;
			}
			prev = ')';
		}
	}
	
	return answer;
}

int main(void) {
	int answer = solution("()(((()())(())()))(())");
	printf("%d", answer);

}