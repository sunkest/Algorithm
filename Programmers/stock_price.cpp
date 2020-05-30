#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;
	
	for (int i = 0; i < prices.size(); i++) {
		for (int j = i + 1; j < prices.size(); j++) {
			if (prices[i] > prices[j]) {	//dec
				answer.push_back(j - i);
				break;
			}
			if (j == prices.size() - 1) {
				answer.push_back(prices.size() - i - 1);
			}
		}
	}
	answer.push_back(0);
	return answer;
}

int main(void) {
	vector<int> answer = solution({ 1,2,4,3,2,3,1,4,3,2,3 });
	for (int i = 0; i < answer.size(); i++) {
		printf("%d ", answer[i]);
	}
}