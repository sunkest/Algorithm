#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

const int MAX = 52 * 20 + 20;
bool p[MAX];

int main(void) {

	//최대는 Z 20개 = 1040
	string str;
	cin >> str;
	int sum = 0;
	for (int i = 0; i < str.length(); i++) {
		int s = 0;
		if (str[i] >= 'a')
			s = 'a' - 1;
		else
			s = 'A' - 27;
		sum += (str[i] - s);
	}

	for (int i = 1; i < MAX; i++)
		p[i] = false;
	for (int i = 2; i < MAX; i++) {
		if (p[i] == false) {
			for (int j = i * i; j < MAX; j += i) {
				p[j] = true;
			}
		}
	}
	if (p[sum])
		printf("It is not a prime word.");
	else
		printf("It is a prime word.");
}
