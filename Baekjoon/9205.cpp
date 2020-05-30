#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Point {
	int x;
	int y;
};

int t, n;
vector<Point> v;
vector<vector<int>> g;
bool* visited;
bool* ans;

int main(void) {
	cin >> t >> n;
	ans = new bool[t];
	for (int i = 0; i < n + 2; i++) {
		visited[i] = false;
	}
	int x, y;
	cin >> x, y;
	Point p = { x, y };
	v.insert(p);

}