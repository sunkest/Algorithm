#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <deque>
using namespace std;

int solution(vector<int> people, int limit) {
	int answer = 0;
	deque<int> dq(people.begin(), people.end());
	sort(dq.begin(), dq.end(), greater<int>());
	while (!dq.empty()) {
		int onboat = 0;
		onboat += dq.front();
		dq.pop_front();
		if (!dq.empty() && dq.back() + onboat <= limit) {
			onboat += dq.back();
			dq.pop_back();
		}
		answer++;
	}


	return answer;
}

int main(void) {
	printf("%d", solution({ 70,50,80,50,20,10,90 }, 100));
}