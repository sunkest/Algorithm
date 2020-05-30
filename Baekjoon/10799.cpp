#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	string str;
	cin >> str;
	stack<char> stk;

	int count = 0;

	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '(') {
			stk.push(str[i]);
		}
		else if (str[i] == ')') {
			stk.pop();
			if (str[i - 1] == '(') {	//레이저
				count += stk.size();
			}
			else {	//파이프 끝
				count++;	
			}
		}
	}

	printf("%d\n", count);
}