#include <iostream>
using namespace std;
void Where(char* strA, char* strB, int t, int n1, int n2);		//개미가 T초뒤에 어떻게 배열되어있는지 구하는 함수
void Reverse(char* str, int n);	//A그룹 배열의 순서를 뒤집어주는 함수
bool ExceptionThrow(char* arrA, char* arrB, int n1, int n2, bool x);	//개미 입력시 예외처리

int main(void) {
	int n1, n2, T;		//A그룹의 개미수 n1, B그룹의 개미수 n2
	char *arrB, *arrA;	//A그룹의 개미 배열 arrA, B그룹의 개미 배열 arrB
	while (1) {
		cin >> n1 >> n2;
		if (cin.fail() || n1 < 1 || n2 < 1) {	//문자나 문자열이 들어간 경우 또는 1보다 적은 수를 입력한 경우
			cout << "양의 정수를 입력해 주세요" << endl;	//안내문구 출력
			cin.clear();	//cin객에 내의 플래그값 초기화
			cin.ignore(100000, '\n');	// 입력버퍼를 '\n'을 만나기 전까지 100000개 문자 초기화
			continue;		//다시 입력
		}
		else break;
	}

	arrB = new char[n2];	//배열 동적할당
	arrA = new char[n1];
	
	do {	//별도 함수 통해서 입력 예외처리 // 오류발생시 재입력 요구
	cin >> arrA; 
	} while (ExceptionThrow(arrA, arrB, n1, n2, 1));
	do {
		cin >> arrB;
	} while (ExceptionThrow(arrA, arrB, n1, n2, 0));

	while (1) {	//몇 초후의 결과를 구할지 입력
		cin >> T;
		if (cin.fail() || T < 0 || T>50) {	//범위에 벗어나거나 정수가 아닌경우 다시 입력요구
			cout << "양의 정수를 입력해 주세요" << endl;
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
	After = new char[n1 + n2];	//T초뒤의 개미들이 배열된 모습을 저장할 배열
	for (int i = 0; i < n1 + n2; i++) {	//배열의 모든값 NULL로 초기화
		After[i] = NULL;
	}

	//A그룹의 개미들이 움직이는 모양이 규칙적으로 움직이므로 T초에 대하여 n1, n2 이용하여 일반적으로 표현 가능
	//제 자리만 찾아서 After 배열에 알맞은 자리에 넣어주면 된다.

	for (int i = 0; i < n1; i++) {
		int n = n1 - i;		//A그룹 개미들을 왼쪽부터 a1 a2 a3로 계산하면 헷갈리므로 a3 a2 a1로 뒤집어서 표현
		if (t < n)		//an 번 개미는 n초부터 한 칸씩 전진 -> n초 이전에는 제자리
			After[i] = strA[i];
		else if (t >= n2 + n - 1) {		//A그룹의 경우 [n2(B그룹 개미수) + (n - 1) ]초 에 최종 목적지 도착 _ 더이상 움직이지 않음
			After[n1 + n2 - n] = strA[i];	//도착지의 인덱스는 n1+n2-n
		}
		else {	//n초(출발) 이후 n2+(n-1)초(도착) 이전 A그룹 n번째 개미의 인덱스는 [n1-n+(t-n+1)] = [n1-2n+t+1]
			After[n1 - 2*n + t + 1] = strA[i];
		}
	}

	//A그룹을 다 넣고나면 B그룹은 복잡하게 계산할 필요 없이 After배열 에서 빈칸에 차례대로 넣으면된다.
	int j = 0;
	for (int i = 0; i < n1+n2; i++) {	
		if (After[i] == NULL) {		//빈 칸을 찾아서
			After[i] = strB[j++];		//차례대로 B그룹 개미들을 하나씩 넣는다.
		}
	}
	for (int i = 0; i < n1 + n2; i++) {
		cout << After[i];	//출력
	}
	cout << endl;
	delete [] After;

	return;
}

void Reverse(char* str, int n) {	//배열 A의 순서를 뒤집어주는 함수
	char temp;
	for (int i = 0; i < n/2; i++) {
		temp = str[n - i - 1];
		str[n - i - 1] = str[i];
		str[i] = temp;
	}
	return;
}

bool ExceptionThrow(char* arrA, char*arrB, int n1, int n2, bool x) {	//개미 입력시 예외처리 //x값에 따라 다르게 동작
	if (x) {	//인자x에 1 전달시 //A그룹 입력 예외처리
		for (int i = 0; i < n1; i++) {
			if (arrA[i] > 'Z' || arrA[i] < 'A') {	//알파벳 대문자가 아닌 문자가 있는지 검사
				cout << "알파벳 대문자로 처음부터 다시 입력해 주세요." << endl;
				cin.clear();
				cin.ignore(100000, '\n');
				return 1;	//실패시 1 반환
			}
			for (int j = 0; j < i; j++) {	//중복되는 문자가 있는지 검사
				if (arrA[i] == arrA[j]) {	//
					cout << "동일한 문자는 여러번 사용할 수 없습니다. 다시 입력해 주세요." << endl;
					return 1;	//실패시 1 반환
				}
			}
		}
	}
	else {	//인자x에 0전달시 // B그룹 입력 예외처리
		for (int i = 0; i < n2; i++) {
			if (arrB[i] > 'Z' || arrB[i] < 'A') {	//알파벳 대문자가 아닌 문자가 있는지 검사
				cout << "알파벳 대문자로 처음부터 다시 입력해 주세요." << endl;
				cin.clear();
				cin.ignore(100000, '\n');
				return 1;	//실패시 1 반환
			}
			for (int j = 0; j < i; j++) {
				if (arrB[i] == arrB[j]) {	//중복되는 문자가 있는지 검사
					cout << "동일한 문자는 여러번 사용할 수 없습니다. 다시 입력해 주세요." << endl;
					return 1;	//실패시 1 반환
				}
			}
			for (int j = 0; j < n1; j++) {
				if (arrB[i] == arrA[j]) {	//A그룹과도 중복되는 문자가 있는지 검사
					cout << "동일한 문자는 여러번 사용할 수 없습니다. 다시 입력해 주세요." << endl;
					return 1;	//실패시 1 반환
				}
			}
		}
	}
	return 0;	//정상 입력 0반환
}