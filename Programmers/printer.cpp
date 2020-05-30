#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 1;
	queue<pair<int, int>> q;
	priority_queue<int> pq;

	for (int i = 0; i < priorities.size(); i++) {
		q.push(make_pair(i, priorities[i]));
		pq.push(priorities[i]);
	}
	while (true) {
		if (pq.top() == q.front().second) {
			if (q.front().first == location) return answer;
			else {
				answer++;
				pq.pop();
				q.pop();
			}
		}
		else {
			q.push(q.front());
			q.pop();
		}
	}

	return -1;
}
int main(void) {

}