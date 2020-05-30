#include <vector>
#include <stack>
#include <iostream>

using namespace std;
int solution(vector<vector<int>> board, vector<int> moves);
int main(void) {
	vector<vector<int>> board = { {0, 0, 0, 0, 0},{0, 0, 1, 0, 3 }, {0, 2, 5, 0, 1},{4, 2, 4, 4, 2},{3, 5, 1, 3, 1} };
	vector<int> moves = { 1, 5, 3, 5, 1, 2, 1, 4 };
	
	int ans = solution(board, moves);
	printf("%d", ans);
	return 0;
}

int solution(vector<vector<int>> board, vector<int> moves) {
	int answer = 0;
	vector<int> top;
	int N = board.size();
	stack<int> stk;

	for (int i = 0; i < N; i++) top.push_back(10);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++){
			if (board[j][i] != 0) {
				top[i] = j;
				break;
			}
		}
	}

	stk.push(-1);
	for (int i = 0; i < moves.size(); i++) {
		int p = moves[i]-1;
		int index = top[p];
		if (top[p] <= N-1) {
			int target = board[index][p];
			if (target != stk.top()) {
				stk.push(target);
				board[index][p] = 0;
				top[p]++;
			}
			else {
				stk.pop();
				answer += 2;
				board[index][p] = 0;
				top[p]++;
			}
		}
		
	}

	return answer;
}