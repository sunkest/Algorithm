#include <iostream>
using namespace std;
void Where(char* strA, char* strB, int t, int n1, int n2);		//���̰� T�ʵڿ� ��� �迭�Ǿ��ִ��� ���ϴ� �Լ�
void Reverse(char* str, int n);	//A�׷� �迭�� ������ �������ִ� �Լ�
bool ExceptionThrow(char* arrA, char* arrB, int n1, int n2, bool x);	//���� �Է½� ����ó��

int main(void) {
	int n1, n2, T;		//A�׷��� ���̼� n1, B�׷��� ���̼� n2
	char *arrB, *arrA;	//A�׷��� ���� �迭 arrA, B�׷��� ���� �迭 arrB
	while (1) {
		cin >> n1 >> n2;
		if (cin.fail() || n1 < 1 || n2 < 1) {	//���ڳ� ���ڿ��� �� ��� �Ǵ� 1���� ���� ���� �Է��� ���
			cout << "���� ������ �Է��� �ּ���" << endl;	//�ȳ����� ���
			cin.clear();	//cin���� ���� �÷��װ� �ʱ�ȭ
			cin.ignore(100000, '\n');	// �Է¹��۸� '\n'�� ������ ������ 100000�� ���� �ʱ�ȭ
			continue;		//�ٽ� �Է�
		}
		else break;
	}

	arrB = new char[n2];	//�迭 �����Ҵ�
	arrA = new char[n1];
	
	do {	//���� �Լ� ���ؼ� �Է� ����ó�� // �����߻��� ���Է� �䱸
	cin >> arrA; 
	} while (ExceptionThrow(arrA, arrB, n1, n2, 1));
	do {
		cin >> arrB;
	} while (ExceptionThrow(arrA, arrB, n1, n2, 0));

	while (1) {	//�� ������ ����� ������ �Է�
		cin >> T;
		if (cin.fail() || T < 0 || T>50) {	//������ ����ų� ������ �ƴѰ�� �ٽ� �Է¿䱸
			cout << "���� ������ �Է��� �ּ���" << endl;
			cin.clear();
			cin.ignore(10000, '\n');
			continue;
		}
		else break;
	}

	Reverse(arrA, n1);
	Where(arrA, arrB, T, n1, n2);

	arrA = { 0 };
	arrB = { 0 };
	delete[]arrB;
	delete[]arrA;

	return 0;
}

void Where(char* strA, char* strB, int t, int n1, int n2) {
	char* After;
	After = new char[n1 + n2];	//T�ʵ��� ���̵��� �迭�� ����� ������ �迭
	for (int i = 0; i < n1 + n2; i++) {	//�迭�� ��簪 NULL�� �ʱ�ȭ
		After[i] = NULL;
	}

	//A�׷��� ���̵��� �����̴� ����� ��Ģ������ �����̹Ƿ� T�ʿ� ���Ͽ� n1, n2 �̿��Ͽ� �Ϲ������� ǥ�� ����
	//�� �ڸ��� ã�Ƽ� After �迭�� �˸��� �ڸ��� �־��ָ� �ȴ�.

	for (int i = 0; i < n1; i++) {
		int n = n1 - i;		//A�׷� ���̵��� ���ʺ��� a1 a2 a3�� ����ϸ� �򰥸��Ƿ� a3 a2 a1�� ����� ǥ��
		if (t < n)		//an �� ���̴� n�ʺ��� �� ĭ�� ���� -> n�� �������� ���ڸ�
			After[i] = strA[i];
		else if (t >= n2 + n - 1) {		//A�׷��� ��� [n2(B�׷� ���̼�) + (n - 1) ]�� �� ���� ������ ���� _ ���̻� �������� ����
			After[n1 + n2 - n] = strA[i];	//�������� �ε����� n1+n2-n
		}
		else {	//n��(���) ���� n2+(n-1)��(����) ���� A�׷� n��° ������ �ε����� [n1-n+(t-n+1)] = [n1-2n+t+1]
			After[n1 - 2*n + t + 1] = strA[i];
		}
	}

	//A�׷��� �� �ְ��� B�׷��� �����ϰ� ����� �ʿ� ���� After�迭 ���� ��ĭ�� ���ʴ�� ������ȴ�.
	int j = 0;
	for (int i = 0; i < n1+n2; i++) {	
		if (After[i] == NULL) {		//�� ĭ�� ã�Ƽ�
			After[i] = strB[j++];		//���ʴ�� B�׷� ���̵��� �ϳ��� �ִ´�.
		}
	}
	for (int i = 0; i < n1 + n2; i++) {
		cout << After[i];	//���
	}
	cout << endl;
	delete [] After;

	return;
}

void Reverse(char* str, int n) {	//�迭 A�� ������ �������ִ� �Լ�
	char temp;
	for (int i = 0; i < n/2; i++) {
		temp = str[n - i - 1];
		str[n - i - 1] = str[i];
		str[i] = temp;
	}
	return;
}

bool ExceptionThrow(char* arrA, char*arrB, int n1, int n2, bool x) {	//���� �Է½� ����ó�� //x���� ���� �ٸ��� ����
	if (x) {	//����x�� 1 ���޽� //A�׷� �Է� ����ó��
		for (int i = 0; i < n1; i++) {
			if (arrA[i] > 'Z' || arrA[i] < 'A') {	//���ĺ� �빮�ڰ� �ƴ� ���ڰ� �ִ��� �˻�
				cout << "���ĺ� �빮�ڷ� ó������ �ٽ� �Է��� �ּ���." << endl;
				cin.clear();
				cin.ignore(100000, '\n');
				return 1;	//���н� 1 ��ȯ
			}
			for (int j = 0; j < i; j++) {	//�ߺ��Ǵ� ���ڰ� �ִ��� �˻�
				if (arrA[i] == arrA[j]) {	//
					cout << "������ ���ڴ� ������ ����� �� �����ϴ�. �ٽ� �Է��� �ּ���." << endl;
					return 1;	//���н� 1 ��ȯ
				}
			}
		}
	}
	else {	//����x�� 0���޽� // B�׷� �Է� ����ó��
		for (int i = 0; i < n2; i++) {
			if (arrB[i] > 'Z' || arrB[i] < 'A') {	//���ĺ� �빮�ڰ� �ƴ� ���ڰ� �ִ��� �˻�
				cout << "���ĺ� �빮�ڷ� ó������ �ٽ� �Է��� �ּ���." << endl;
				cin.clear();
				cin.ignore(100000, '\n');
				return 1;	//���н� 1 ��ȯ
			}
			for (int j = 0; j < i; j++) {
				if (arrB[i] == arrB[j]) {	//�ߺ��Ǵ� ���ڰ� �ִ��� �˻�
					cout << "������ ���ڴ� ������ ����� �� �����ϴ�. �ٽ� �Է��� �ּ���." << endl;
					return 1;	//���н� 1 ��ȯ
				}
			}
			for (int j = 0; j < n1; j++) {
				if (arrB[i] == arrA[j]) {	//A�׷���� �ߺ��Ǵ� ���ڰ� �ִ��� �˻�
					cout << "������ ���ڴ� ������ ����� �� �����ϴ�. �ٽ� �Է��� �ּ���." << endl;
					return 1;	//���н� 1 ��ȯ
				}
			}
		}
	}
	return 0;	//���� �Է� 0��ȯ
}