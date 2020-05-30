#include <string>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

int solution(vector<int> scoville, int K) {
	priority_queue<int, vector<int>, greater<int>> pq;
	for (int i = 0; i < scoville.size(); i++) {
		pq.push(scoville[i]);
	}
	int count = 0;
	while (!pq.empty()) {
		if (pq.top() < K) {
			if (count == scoville.size() - 1) {
				return -1;
			}
			int a = pq.top();
			pq.pop();
			int b = pq.top();
			pq.pop();
			pq.push(a + (2 * b));
			count++;
		}
		else {
			return count;
		}
	}
}