#include <iostream>
using namespace std;
int HowManyTeams(int n, int m, int k);	
//n명의 여학생, m명의 남학생, k명의 인턴 참여인원이 주어질 때 만들 수 있는 최대의 팀 수를 구하는 함수
void ExceptionThrow(int*n, int*m, int*k); //입력과 예외처리를 받는 함수

int main(void) {
	int n, m, k;	//n=여학생수, m=남학생수, k=인턴수

	ExceptionThrow(&n, &m, &k);
	cout << HowManyTeams(n, m, k);
}

//n명의 여학생, m명의 남학생, k명의 인턴 참여인원이 주어질 때 만들 수 있는 최대의 팀 수를 구하는 함수
//while
int HowManyTeams(int n, int m, int k) {	
	int teams = 0;	//만들 수 있는 팀 수를 저장
	while (1) {	//while루프를 이용해서 
		if ((m + n > k) && (m>0) && (n>1)) {	//남은 학생수가 인턴참여인원보다 크고, 남학생이 1명, 여학생이 2명 이상 남아 최소 한 팀을 만들 수 있는경우
			m--;	//남학생 1명
			n -= 2;	//여학생 2명
			++teams;		//1개의 팀 결성
		}
		else if (m + n == k) return teams;	
		// 남은 인원이 인턴참가인원과 같은 경우 남은인원 모두가 인턴에 참가해야하므로 현재 팀 개수 return
		else if ((m + n > k) && (m == 0 || n <= 1)) return teams;
		//남은 인원이 인턴 참가인원 보다는 많지만 남학생이 없거나 여학생이 1명이하여서 팀을 만들 수 없는경우 현재 팀 개수 return
		else return --teams; 
		//그 외의 경우(남은 인원수가 인턴참가인원보다 적은 경우) 
		//-> 반복문을 돌며 팀을 만들어내는 과정에서 마지막으로 팀을 만든 직후 m+n<k가 된 경우 인턴 참가가 최우선 이기 때문에 팀을 하나 해체하여 인턴으로 돌려야한다.
	}
}

void ExceptionThrow(int*n, int*m, int*k) {	//입력과 예외처리를 담당하는 함수
	while (1) {
		cin >> *n >> *m >> *k;
		if (cin.fail()) {	//cin.fail() int형 변수에 char형 문자형 등이 들어가는 경우 오류로 판단하여 true반환
			cout << "값을 범위에 맞도록 입력하세요(0 <= n <= 100) (0 <= m <= 100) (0 <= k <= m+n)"  << endl;
			cin.clear();	//문자열 입력시 cin객체 내부의 플래그값이 변경되는데, 이 값을 초기화
			cin.ignore(100000, '\n');	//입력버퍼 100000개 문자만큼, 단, '\n'을 만날때 까지만 초기화
			continue;	//다시 입력요구
		}
		else if ((0 <= *n) && (*n <= 100) && (0 <= *m) && (*m <= 100) && (*k>=0) && (*k<=*m + *n)) break;
		else {
			cout << "값을 범위에 맞도록 입력하세요(0 <= n <= 100) (0 <= m <= 100) (0 <= k <= m+n)"  << endl;
			continue;
		}
	}
}