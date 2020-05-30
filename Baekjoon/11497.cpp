#include <iostream>
#include <vector>
using namespace std;
#define MIN 1
#define MAX 100
int M(int* str, int length);		//�볪�� �ִ�(���� ��) ����ϴ� �Լ�
void quicksort(int arr[], int left, int right);	//�迭�� ������ ������������ ����
void Swap(int arr[], int a, int b);	//�����Ҷ� ����ϴ� �Լ�
int ExeptionThrow(int min, int max);	//�Է� ����ó���� �Լ�
int GetHeight(int arr[], int len);	//�볪�� ���� �Է�

//�׽�Ʈ���̽� ��ŭ �ݺ� -> ���� �迭, ��� �迭 �����Ҵ� -> (���� �Է� -> �볪�� ���� �迭 �����Ҵ� -> ��� -> ��� �迭�� ����):Tȸ�ݺ� -> ����迭 ���

int main(void) {
	int T;	//�׽�Ʈ���̽� ����
	int length;	//�볪�� ����
	vector<int> ans;	//������� ������ ����

	cout << "�׽�Ʈ���̽��� ������ �Է����ּ���(1<=T<=100000)" << endl;
	T = ExeptionThrow(MIN, MAX);	//T�� �׽�Ʈ���̽� �Է¹���

	for (int i = 0; i < T; i++) {		//T��ŭ �ݺ�
		cout << "�볪���� ������ �Է����ּ���(5<=N<=10000)" << endl;
		length = ExeptionThrow(5, 10000);	//�볪�� ���� �Է¹���
		
		int* str = new int[length];		//�볪�� ������ŭ str �迭 �����Ҵ�
		cout << "�볪������ ���̸� �Է��� �ּ���" << endl;
		while (GetHeight(str, length)) {	//�볪�� ���̹޴°� ���� �������� �ѹ��� �޾ƾ��ؼ� �ϳ��� �������� ��߳��� ó������ �ٽ� �Է��ϰ� ����.
			continue;
		}

		ans.push_back(M(str, length));	//���Ϳ� i��° �׽�Ʈ���̽��� ���� �߰�
		delete[] str;	//�����Ҵ� ����
	}
	for (int i = 0; i < T; i++) cout << ans[i] << endl;	//���� ���ʴ�� ���

	return 0;
}

int ExeptionThrow(int min, int max) {	//�׽�Ʈ���̽�, �볪�� ���� �Է½� ����ó�����ִ� �Լ�
	int n;
	while (1) {
		cin >> n;
		if (cin.fail()) {
			cout << "������ �´� �ڿ����� �Է����ּ���" << endl;
			cin.clear();
			cin.ignore(100000, '\n');
			continue;
		}
		else if (n >= min && n<=max ) break;
		else {
			cout << "������ �´� �ڿ����� �Է����ּ���" << endl;
			continue;
		}
	}
	return n;
}

int GetHeight(int arr[], int len) {		//�볪���� ���� �Է¹����� ����ó�� ���ִ� �Լ�
	for (int i = 0; i < len; i++) {
		cin >> arr[i];
		if (cin.fail() || arr[i] < 1 || arr[i] > 100000) {
			cout << "�볪���� ���̴� 1�̻� 100,000 �����Դϴ�. ó������ �ٽ� �Է��ϼ���" << endl;
			cin.clear();
			cin.ignore(10000, '\n');
			i = 0;
			for (int j = 0; j < len; j++) arr[j] = 1;
			return 1;
		}
	}
	return 0;
}

int M(int* str, int length) {	//���� �ִ� ����ϴ� �Լ�
	quicksort(str, 0, length-1);	//�Է¹��� �볪�� ���̵��� ������������ ����
	int max = 0;		//�ִ� ���� ���� = ��
	for (int i = 2; i < length; i++) {	//i�� 0, 1�϶��� �ǹ� �����Ƿ� 2���� �˻�
		if (max < str[i] - str[i - 2]) {	//�볪���� �������� �迭�ߴٰ� ������ 
			max = str[i] - str[i - 2];	//��ĭ ���̳��� �����鳢���� ���� ��� ���ؼ� ���� �� ū���� max�� ����
		}
	}
	return max;	//���� ��ȯ
}

void quicksort(int arr[], int left, int right) {		//�� ��Ʈ_�迭�� �������� ����
	if (left >= right) {
		return;
	}
	int pivot = left;
	int low = left + 1;
	int high = right;

	while (low <= high) {
		while (arr[low] <= arr[pivot] && low <= right) {
			low++;
		}
		while (arr[high] >= arr[pivot] && high > left) {
			high--;
		}
		if (low > high) {
			Swap(arr, pivot, high);
		}
		else {
			Swap(arr, low, high);
		}
	}
	pivot = high;
	quicksort(arr, left, pivot - 1);
	quicksort(arr, pivot + 1, right);
}

void Swap(int arr[], int a, int b) {	//���� �Լ�_����Ʈ���� ���
	int temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;
}