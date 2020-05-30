#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;
	for (int i = 0; i < commands.size(); i++) {
		int start = commands[i][0] - 1;
		int end = commands[i][1] - 1;
		int index = commands[i][2] -1;
		vector<int> arr;
		for (int j = start; j <= end; j++) {
			arr.push_back(array[j]);
		}
		sort(arr.begin(), arr.end());
		answer.push_back(arr[index]);
	}
	return answer;
}

int main(void) {
	vector<int> array = { 1,5,2,6,3,7,4 };
	vector<vector<int>> commands = { {2,5,3}, {4,4,1}, {1,7,3} };
	
	vector<int> answer = solution(array, commands);
	for (int i = 0; i < answer.size(); i++) {
		printf("%d ", answer[i]);
	}
}