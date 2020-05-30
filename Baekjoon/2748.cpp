#include <iostream>
using namespace std;
#define MAX 90
#define MIN 1
long long Fibonacci(int n);	//n��° �Ǻ���ġ ���� ���ϴ� �Լ�
int ExceptionThrow(int min, int max);	//�Է��� ó���ϸ�, ����ó���� �����ϴ� �Լ�

int main(void) {
	int n;

	n = ExceptionThrow(MIN, MAX);	//n�� �Է� �� ��ȯ
	cout << Fibonacci(n) << endl;	//1�̻� 90������ �Է¿� ���ؼ� n��° �Ǻ���ġ ���� ���

	return 0;
}

//�ݺ����� �̿��Ͽ� ����Լ��� �̿������� ���� �ð����⵵�� �޸� ��뷮�� ũ�� ���δ�. 

long long Fibonacci(int n) {	//n��° �Ǻ���ġ ���� ����ϴ� �Լ� // 90��° �Ǻ���ġ�� ���� ��ƾ� �ϹǷ� long long Ÿ���� ����ߴ�.
	long long Fibo[2] = { 0, 1 };	//n��° �Ǻ���ġ ���� ����Ѵٰ� ���� �� �ٷ� �� �װ� �� ���� �� ���׸� ������ ���� �� �ִ�. // 0��°�� 0, 1��°�� 1�� �ʱ�ȭ
	for (int i = 2; i <= n; i++) {
		long long temp = Fibo[0];	//�ӽ� ������ n-2��° �� ����
		Fibo[0] = Fibo[1];	//n-1��° ���� ù ĭ�� �̵�
		Fibo[1] = temp + Fibo[1];	//�ι�° ĭ�� n��° �� ����
	} //ù��° ���� for���� �������� �����Ƿ� �ڿ������� 1 return
	return Fibo[1];	//n��° �� ��ȯ
}

int ExceptionThrow(int min, int max) {
	double n;	//double������ �Է¹޾Ƽ� �Ʒ����� �Ǽ� ����ó��
	while (1) {
		cin >> n;
		if (cin.fail()) {	//cin.fail() : �Է¿��� ������ �߻��ϸ� true ��ȯ. n�� double ���̹Ƿ� char�� ���ڰ� �� ��� true ��ȯ.
			cout << "90 ������ �ڿ����� �Է��� �ּ���" << endl;
			cin.clear(); //cin.clear() : cin��ü ������ flag���� �ʱ�ȭ	//���ڿ��� �ԷµȰ�� cin���� ���ѷ����� ���۵Ǵ� ������ �ذ�
			cin.ignore(100000, '\n'); //�Է� ���� ���� ���� 100000�� ���ڸ�ŭ, �Ǵ� '\n'�� ������ ���� ����. �ܼ�â���� �Է½ÿ� enterŰ�� �̿��� �Է¹޴� Ư�� �̿�
			continue;	//�Է��� �ٽù޾� �������� �Է��� �� �� ���� �ݺ�
		}
		else if (n >= min && n <= max) {
			if (n - (int)n == 0) {	//������ �ƴ� ���
				break;		//���ڷ� ���޹��� min�̻� max������ �ڿ����� ��� break�� ���� while���� Ż��
			}
			else {
				cout << "90 ������ �ڿ����� �Է��� �ּ���" << endl;
				continue;		//�ٽ� �Է� �䱸
			}
		}
		else {	//�� ���� ���
			cout << "90 ������ �ڿ����� �Է��� �ּ���" << endl;
			continue;	//�ٽ� �Է¹޵��� �ݺ�
		}
	}
	return (int)n;
}