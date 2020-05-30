#include <string>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int solution(vector<int> citations) {
	int answer = 0;
	sort(citations.begin(), citations.end(), greater<int>());
	for (int i = 0; i < citations.size(); i++) {
		if (i + 1 <= citations[i]) {
			answer = i + 1;
		}
	}

	return answer;
}

int main(void) {
	vector<int> citations = { 3,0,6,1,5 };
	printf("%d", solution(citations));
}