#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

void DFS(int i, int j, int c);

bool v[100][100] = { 0, };
int map[100][100];
int N;
struct p {
	int x;
	int y;
	int c;
};
vector<p> vec;
int main(void) {

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}

	//DFS
	int count = 2;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!v[i][j] && map[i][j] == 1) {
				DFS(i, j, ++count);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (map[i][j] != 0) {
				p a;
				a.x = i;
				a.y = j;
				a.c = map[i][j];
				vec.push_back(a);
			}
		}
	}

	int min = 99999;
	for (int i = 0; i < vec.size(); i++) {
		for (int j = i; j < vec.size(); j++) {
			if (vec[i].c != vec[j].c) {
				int d = abs(vec[i].x - vec[j].x) + abs(vec[i].y - vec[j].y) - 1;
				if (d < min) min = d;
			}
		}
	}

	printf("%d\n", min);
}

void DFS(int i, int j, int c) {
	if (i >= 0 && j >= 0 && i < N && j < N && !v[i][j]) {
		v[i][j] = true;
		if (map[i][j] == 1) {
			map[i][j] = c;
				DFS(i + 1, j, c);
				DFS(i - 1, j, c);
				DFS(i, j + 1, c);
				DFS(i, j - 1, c);
			}
		else return;
	}
	else return;
}
