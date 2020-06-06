#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<vector<int>> map = { {0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38},	//route0	//10 (0,5)->route1, 20 (0,10)->route2, 30 (0,15)->route3, 38 (0,19) -> 40(4,2)
										{13,16,19},		//route1	//19 (1,2)->25 (3,3)
										{22,24},			//route2	//24 (2,1)->25 (3,3)
										{28,27,26,25},	//route3	//25 (3,3)->route4
										{30,35,40,0}};	//route4	//(4,3) = finish point
int scores[] = { 0,0,0,0 };
int pos[4][2] = { { 0,0 },{ 0,0 },{ 0,0 },{ 0,0 } }; 	//[route, index]
int answer = 0;
vector<int> input;
void dfs(int depth) {
	//��������
	if (depth == 10) {
		int sum = 0;
		for (int i = 0; i < 4; i++) {
			sum += scores[i];
		}
		answer = max(sum, answer);
		//printf("return, %d\n", answer);
		return;
	}
	//Ž��
	int move = input[depth];
	for (int i = 0; i < 4; i++) {
		int r = pos[i][0]; int p = pos[i][1];
		//printf("(%d, %d), (%d, %d), (%d, %d), (%d, %d)\n", pos[0][0], pos[0][1], pos[1][0], pos[1][1], pos[2][0], pos[2][1], pos[3][0], pos[3][1]);
		int new_r = r; int new_p = p;
		//������ Ȯ��
		if (r == 4 && p==3) continue;
		//�̵�����
		for (int k = 0; k < move; k++) {
			if (k==0 && r == 0 && p == 5) { new_r = 1; new_p = 0; }//
			else if (k == 0 && r == 0 && p == 10) { new_r = 2; new_p = 0; }//
			else if (k == 0 && r == 0 && p == 15) { new_r = 3; new_p = 0; }//
			else if (new_r == 1 && new_p == 2) { new_r = 3; new_p = 3; }
			else if (new_r == 2 && new_p == 1) { new_r = 3; new_p = 3; }
			else if (new_r == 3 && new_p == 3) { new_r = 4; new_p = 0; }
			else if (new_r == 0 && new_p == 19) { new_r = 4; new_p = 2; }
			else if (new_r == 4 && new_p == 3) { break; }
			else {
				new_p++;
			}
		}
		//�� �ߺ�����
		bool flag = false;
		for (int k = 0; k < 4; k++) {
			if (k == i) continue;
			if (new_r == 4 && new_p == 3) break;
			if (new_r == pos[k][0] && new_p == pos[k][1]) flag = true;
		}
		if (flag) continue;
		//�� �̵� confirm, ���� ����
		pos[i][0] = new_r; pos[i][1] = new_p;
		int temp = scores[i];
		scores[i] += map[new_r][new_p];
		//���� dfs ȣ��
		dfs(depth + 1);
		//��, ���� ���󺹱�
		pos[i][0] = r; pos[i][1] = p;
		scores[i] = temp;
	}
}


int main(void) {
	for (int i = 0; i < 10; i++) {
		int n;
		cin >> n;
		input.push_back(n);
	}
	dfs(0);
	printf("%d", answer);
}