#include <iostream>
#include <stdlib.h>
using namespace std;
int P(int n);

int main(void) {
	int T;
	int n;
	while (1) {
		cout << "�׽�Ʈ ���̽��� ������ �Է��ϼ���\n" << endl;
		cin >> T;
		if (cin.fail()) {
			cout << "���� ������ �Է����ּ���" << endl;
			cin.clear();
			cin.ignore();
			continue;
		}
		if (T > 0) break;
		else {
			cout << "���� ������ �Է����ּ���" << endl;
			continue;
		}
	}
	for (int i = 0; i < T; i++)
	{
		cout << "����n�� �Է����ּ���" << endl;
		cin >> n;
		if (cin.fail()) {
			cout << "11���� ���� ���� ������ �Է����ּ���" << endl;
			i--;
			cin.clear();
			cin.ignore();
			continue;
		}
		if (n > 0 && n < 11) {
			cout << P(n) << endl << endl;
			continue;
		}
		else {
			cout << "11���� ���� ���� ������ �Է��ϼ���" << endl;
			i--;
			cin.clear();
			continue;
		}
	}
	system("pause");
	return 0;
}

int P(int n) {
	if (n == 1) return 1;
	else if (n == 2) return 2;
	else if (n == 3) return 4;
	else return P(n - 3) + P(n - 2) + P(n - 1);
}
