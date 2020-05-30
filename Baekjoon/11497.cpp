#include <iostream>
#include <vector>
using namespace std;
#define MIN 1
#define MAX 100
int M(int* str, int length);		//통나무 최댓값(실제 답) 계산하는 함수
void quicksort(int arr[], int left, int right);	//배열의 값들을 오름차순으로 정렬
void Swap(int arr[], int a, int b);	//정렬할때 사용하는 함수
int ExeptionThrow(int min, int max);	//입력 예외처리용 함수
int GetHeight(int arr[], int len);	//통나무 높이 입력

//테스트케이스 만큼 반복 -> 개수 배열, 결과 배열 동적할당 -> (개수 입력 -> 통나무 높이 배열 동적할당 -> 계산 -> 결과 배열에 저장):T회반복 -> 결과배열 출력

int main(void) {
	int T;	//테스트케이스 개수
	int length;	//통나무 개수
	vector<int> ans;	//정답들을 저장할 벡터

	cout << "테스트케이스의 개수를 입력해주세요(1<=T<=100000)" << endl;
	T = ExeptionThrow(MIN, MAX);	//T에 테스트케이스 입력받음

	for (int i = 0; i < T; i++) {		//T만큼 반복
		cout << "통나무의 개수를 입력해주세요(5<=N<=10000)" << endl;
		length = ExeptionThrow(5, 10000);	//통나무 개수 입력받음
		
		int* str = new int[length];		//통나무 개수만큼 str 배열 동적할당
		cout << "통나무들의 높이를 입력해 주세요" << endl;
		while (GetHeight(str, length)) {	//통나무 높이받는건 숫자 여러개를 한번에 받아야해서 하나라도 범위에서 어긋나면 처음부터 다시 입력하게 만듬.
			continue;
		}

		ans.push_back(M(str, length));	//벡터에 i번째 테스트케이스의 정답 추가
		delete[] str;	//동적할당 해제
	}
	for (int i = 0; i < T; i++) cout << ans[i] << endl;	//정답 차례대로 출력

	return 0;
}

int ExeptionThrow(int min, int max) {	//테스트케이스, 통나무 개수 입력시 예외처리해주는 함수
	int n;
	while (1) {
		cin >> n;
		if (cin.fail()) {
			cout << "범위에 맞는 자연수를 입력해주세요" << endl;
			cin.clear();
			cin.ignore(100000, '\n');
			continue;
		}
		else if (n >= min && n<=max ) break;
		else {
			cout << "범위에 맞는 자연수를 입력해주세요" << endl;
			continue;
		}
	}
	return n;
}

int GetHeight(int arr[], int len) {		//통나무들 높이 입력받을때 예외처리 해주는 함수
	for (int i = 0; i < len; i++) {
		cin >> arr[i];
		if (cin.fail() || arr[i] < 1 || arr[i] > 100000) {
			cout << "통나무의 높이는 1이상 100,000 이하입니다. 처음부터 다시 입력하세요" << endl;
			cin.clear();
			cin.ignore(10000, '\n');
			i = 0;
			for (int j = 0; j < len; j++) arr[j] = 1;
			return 1;
		}
	}
	return 0;
}

int M(int* str, int length) {	//실제 최댓값 계산하는 함수
	quicksort(str, 0, length-1);	//입력받은 통나무 높이들을 오름차순으로 정렬
	int max = 0;		//최댓값 담을 변수 = 답
	for (int i = 2; i < length; i++) {	//i는 0, 1일때는 의미 없으므로 2부터 검사
		if (max < str[i] - str[i - 2]) {	//통나무를 원형으로 배열했다고 했을때 
			max = str[i] - str[i - 2];	//두칸 차이나는 나무들끼리의 차를 모두 구해서 그중 젤 큰값을 max에 넣음
		}
	}
	return max;	//정답 반환
}

void quicksort(int arr[], int left, int right) {		//퀵 소트_배열을 오름차순 정렬
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

void Swap(int arr[], int a, int b) {	//스왑 함수_퀵소트에서 사용
	int temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;
}