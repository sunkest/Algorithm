#include <iostream>
using namespace std;
#define MAX 90
#define MIN 1
long long Fibonacci(int n);	//n번째 피보나치 수를 구하는 함수
int ExceptionThrow(int min, int max);	//입력을 처리하며, 예외처리를 포함하는 함수

int main(void) {
	int n;

	n = ExceptionThrow(MIN, MAX);	//n에 입력 값 반환
	cout << Fibonacci(n) << endl;	//1이상 90이하의 입력에 대해서 n번째 피보나치 수를 출력

	return 0;
}

//반복문을 이용하여 재귀함수를 이용했을때 보다 시간복잡도와 메모리 사용량을 크게 줄인다. 

long long Fibonacci(int n) {	//n번째 피보나치 수를 계산하는 함수 // 90번째 피보나치수 까지 담아야 하므로 long long 타입을 사용했다.
	long long Fibo[2] = { 0, 1 };	//n번째 피보나치 수를 계산한다고 했을 때 바로 전 항과 그 전항 단 두항만 있으면 구할 수 있다. // 0번째는 0, 1번째는 1로 초기화
	for (int i = 2; i <= n; i++) {
		long long temp = Fibo[0];	//임시 변수에 n-2번째 항 저장
		Fibo[0] = Fibo[1];	//n-1번째 항을 첫 칸에 이동
		Fibo[1] = temp + Fibo[1];	//두번째 칸에 n번째 항 저장
	} //첫번째 항은 for문에 진입하지 않으므로 자연스럽게 1 return
	return Fibo[1];	//n번째 항 반환
}

int ExceptionThrow(int min, int max) {
	double n;	//double형으로 입력받아서 아래에서 실수 예외처리
	while (1) {
		cin >> n;
		if (cin.fail()) {	//cin.fail() : 입력에서 오류가 발생하면 true 반환. n이 double 형이므로 char형 문자가 들어갈 경우 true 반환.
			cout << "90 이하의 자연수를 입력해 주세요" << endl;
			cin.clear(); //cin.clear() : cin객체 내부의 flag값을 초기화	//문자열이 입력된경우 cin에서 무한루프가 시작되는 문제를 해결
			cin.ignore(100000, '\n'); //입력 버퍼 내의 값을 100000개 문자만큼, 또는 '\n'을 만날때 까지 비운다. 콘솔창에서 입력시에 enter키를 이용해 입력받는 특성 이용
			continue;	//입력을 다시받아 정상적인 입력이 될 때 까지 반복
		}
		else if (n >= min && n <= max) {
			if (n - (int)n == 0) {	//정수가 아닌 경우
				break;		//인자로 전달받은 min이상 max이하의 자연수인 경우 break를 통해 while루프 탈출
			}
			else {
				cout << "90 이하의 자연수를 입력해 주세요" << endl;
				continue;		//다시 입력 요구
			}
		}
		else {	//그 외의 경우
			cout << "90 이하의 자연수를 입력해 주세요" << endl;
			continue;	//다시 입력받도록 반복
		}
	}
	return (int)n;
}