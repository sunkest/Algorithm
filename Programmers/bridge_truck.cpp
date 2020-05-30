#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	int index = 0;
	queue<int> q;
	int total_weight = 0;
	int finish = 0;
	for (int i = 0; true; i++) {
		if (q.size() == bridge_length) {
			if (q.front() != 0) {
				if (++finish == truck_weights.size()) {
					answer = i;
					break;
				}
			}
			total_weight -= q.front();
			q.pop();
		}
		
		if (total_weight + truck_weights[index] <= weight) {
			q.push(truck_weights[index]);
			if (index == truck_weights.size() - 1) return i + 1 + bridge_length;
			total_weight += truck_weights[index];
			index++;
		} else {
			q.push(0);
		}

	}

	return answer;
}

int main(void) {
	int answer = solution(100, 100, { 10,10,10,10,10,10,10,10,10,10 });
	cout << answer;
}