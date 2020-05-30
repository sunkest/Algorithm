#include <iostream>
#include <vector>
using namespace std;
void Perfect(int n);	//n이 완전수인지 판별하는 함수
int HowMany(int n); //n의 약수의 개수를 계산하는 함수
void GetD(int n, int* arr, int t); //n의 약수들을 모두 구해 t(약수의 개수)만큼 동적할당 된 배열 arr에 저장


int main(void) {
	vector<int> v;
	int n;
	cout << "-1을 입력하면 종료됩니다." << endl;	//안내문구 출력
	while (1) {
		cin >> n;
		if (cin.fail() || (n<=2 && n != -1) || n >= 100000) {	//숫자가 아닌 문자나 범위를 벗어난 수를 입력한 경우
			cout << "2 초과 100,000 미만의 양의 정수를 입력해주세요" << endl;	//안내문자 출력
			cin.clear();	//cin객체의 플래그 값 초기화 -> 문자 입력시 무한루프가 도는 문제 해결
			cin.ignore(100000, '\n');	//입력버퍼 삭제. 100000개 문자만큼, 단 '\n'을 만날때 까지 삭제
			continue;	//다시 입력받는다.
		}
		if(n > 2) 	v.push_back(n);	//벡터에 n추가
		else if (n == -1) break;	//-1입력시 입력 종료
	}

	for (unsigned int i = 0; i < v.size(); i++) {
		Perfect(v[i]);
	}

	return 0;
}

void Perfect(int n) {	//n이 완전수인지 판별
	int sum = 0;	//약수들의 합 저장할 변수
	int t = HowMany(n);	//약수의 개수 저장
	int* arr = new int[t];	//약수들을 저장할 배열 동적할당

	GetD(n, arr, t);	//약수들을 arr에 저장
	
	for (int i = 0; i < t - 1; i++) {	//구한 약수들을 모두 더한다.
		sum += arr[i];
	}

	if (sum == n) {	//n의 약수들의 합이 n과 같은경우
		cout << n << " = " << arr[0];	// n = 1 + ... + n형태로 약수들 출력 시작
		for (int i = 1; i < t - 1; i++) {
			cout << " + " << arr[i];
		}
		cout << endl;
	}
	else {	//아닌 경우 완전수가 아니라고 출력
		cout << n << " is NOT perfect" << endl;
	}

	delete[] arr;	//동적할당 해제
	return;
}

void GetD(int n, int* arr, int t) {	//약수를 모두 구해 arr에 저장하는 함수	//t는 n의 약수의 개수
	int j = 0;

	for (int i = 1; i < sqrt(n); i++) {	//1부터 루트n까지 확인
		if (n%i == 0) {
			arr[j] = i;	
			arr[t - 1 - j++] = n / i;		//배열에 약수를 저장
		}
	}

	return;
}

int HowMany(int n) {	//n의 약수의 개수를 얻는 함수
	int num = 0;	//약수의 개수를 저장할 변수 초기화
	for (int i = 1; i < sqrt(n); i++) {	//1~sqrt(n)까지 확인, 짝이 되는 수까지 포함하여 2개씩 더해준다.
		if (n%i == 0) num += 2;
	}
	if (sqrt(n) * sqrt(n) == n) num--;		//제곱수의 경우 한개 빼줘야한다.

	return num;	// 약수 개수 반환
}