#include <iostream>
using namespace std;

int Howmany(int w);

int main() {
	int w;
	while (1) {
		cin >> w;
		if (cin.fail()) {
			cout << "���� ������ �Է����ּ���" << endl;
			cin.clear();
			cin.ignore(10000, '\n');
			continue;
		}
		else if (w >= 3 && w <= 5000) break;
		else {
			cout << "���� ������ �Է����ּ���" << endl;
			continue;
		}
	}

	cout << Howmany(w) << endl;
	return 0;
}

int Howmany(int w) {
	int n = -1;
	for (int i = 0; 5 * i <= w; i++) {
		if ((w - i * 5) % 3 == 0) {
			int a = i;
			int b = (w - i * 5) / 3;
			if (a + b < n || n == -1) n = a + b;
		}
	}
	return n;
}