#include <iostream>
#include <vector>
using namespace std;
void Perfect(int n);	//n�� ���������� �Ǻ��ϴ� �Լ�
int HowMany(int n); //n�� ����� ������ ����ϴ� �Լ�
void GetD(int n, int* arr, int t); //n�� ������� ��� ���� t(����� ����)��ŭ �����Ҵ� �� �迭 arr�� ����


int main(void) {
	vector<int> v;
	int n;
	cout << "-1�� �Է��ϸ� ����˴ϴ�." << endl;	//�ȳ����� ���
	while (1) {
		cin >> n;
		if (cin.fail() || (n<=2 && n != -1) || n >= 100000) {	//���ڰ� �ƴ� ���ڳ� ������ ��� ���� �Է��� ���
			cout << "2 �ʰ� 100,000 �̸��� ���� ������ �Է����ּ���" << endl;	//�ȳ����� ���
			cin.clear();	//cin��ü�� �÷��� �� �ʱ�ȭ -> ���� �Է½� ���ѷ����� ���� ���� �ذ�
			cin.ignore(100000, '\n');	//�Է¹��� ����. 100000�� ���ڸ�ŭ, �� '\n'�� ������ ���� ����
			continue;	//�ٽ� �Է¹޴´�.
		}
		if(n > 2) 	v.push_back(n);	//���Ϳ� n�߰�
		else if (n == -1) break;	//-1�Է½� �Է� ����
	}

	for (unsigned int i = 0; i < v.size(); i++) {
		Perfect(v[i]);
	}

	return 0;
}

void Perfect(int n) {	//n�� ���������� �Ǻ�
	int sum = 0;	//������� �� ������ ����
	int t = HowMany(n);	//����� ���� ����
	int* arr = new int[t];	//������� ������ �迭 �����Ҵ�

	GetD(n, arr, t);	//������� arr�� ����
	
	for (int i = 0; i < t - 1; i++) {	//���� ������� ��� ���Ѵ�.
		sum += arr[i];
	}

	if (sum == n) {	//n�� ������� ���� n�� �������
		cout << n << " = " << arr[0];	// n = 1 + ... + n���·� ����� ��� ����
		for (int i = 1; i < t - 1; i++) {
			cout << " + " << arr[i];
		}
		cout << endl;
	}
	else {	//�ƴ� ��� �������� �ƴ϶�� ���
		cout << n << " is NOT perfect" << endl;
	}

	delete[] arr;	//�����Ҵ� ����
	return;
}

void GetD(int n, int* arr, int t) {	//����� ��� ���� arr�� �����ϴ� �Լ�	//t�� n�� ����� ����
	int j = 0;

	for (int i = 1; i < sqrt(n); i++) {	//1���� ��Ʈn���� Ȯ��
		if (n%i == 0) {
			arr[j] = i;	
			arr[t - 1 - j++] = n / i;		//�迭�� ����� ����
		}
	}

	return;
}

int HowMany(int n) {	//n�� ����� ������ ��� �Լ�
	int num = 0;	//����� ������ ������ ���� �ʱ�ȭ
	for (int i = 1; i < sqrt(n); i++) {	//1~sqrt(n)���� Ȯ��, ¦�� �Ǵ� ������ �����Ͽ� 2���� �����ش�.
		if (n%i == 0) num += 2;
	}
	if (sqrt(n) * sqrt(n) == n) num--;		//�������� ��� �Ѱ� ������Ѵ�.

	return num;	// ��� ���� ��ȯ
}