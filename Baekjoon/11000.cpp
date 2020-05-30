#include <iostream>
#include <algorithm>
#include <queue>
#include <functional>
#include <vector>
using namespace std;

vector<pair<int, int>> v;	//강의 저장할 벡터
priority_queue<int, vector<int>, greater<int>> q;	//강의실별로 종료시간 넣는 우선순위큐

int main(void) {
	int n;
	cin >> n;
	v.resize(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i].first >> v[i].second;
	}
	sort(v.begin(), v.end());	//입력다받으면 강의 시작시간 기준으로 벡터 정렬

	//첫번째꺼는 먼저 넣기
	q.push(v[0].second);

	for (int i = 1; i < v.size(); i++) {		//강의 하나씩 확인
												//우선순위큐의 top(가장 빨리 끝나는 강의 시간)과 i번째 강의 시작시간 비교
		if (v[i].first >= q.top()) {		//가장빨리끝나는 강의 보다 늦게 시작하는 경우
			q.pop();	//pop하고
			q.push(v[i].second);	//새 강의 종료시간 push
		}
		else q.push(v[i].second);	//사용가능한 강의실 없는 경우 새 강의실로 push
	}

	printf("%d\n", q.size());	//마지막에 큐 사이즈가 강의실 수

}