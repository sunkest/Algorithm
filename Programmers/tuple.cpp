#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct node {
public:
	int num;
	node* parent;
	vector<node*> child;
};

class Tree {
public:
	node root;

	void init(vector<pair<int, int>> path) {
		root.num = 0;
		root.parent = NULL;
		for (int i = 0; i < path.size(); i++) {
			int p = path[i].first;
			int c = path[i].second;
			

		}
	}
};

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
	return (a.first < b.first);
}

int main(void) {
	int n;
	vector<vector<int>> path = {{0, 1}, {0, 3}, {0, 7}, {8, 1}, {3, 6}, {1, 2}, {4, 7}, {7, 5}};
	vector<vector<int>> order = {{8,5},{6,7},{4,1}};
	vector<pair<int, int>> paired;
	for (int i = 0; i < path.size(); i++) {
		pair<int, int> p;
		p.first = path[i][0];
		p.second = path[i][1];
		paired.push_back(p);
	}
	sort(paired.begin(), paired.end(), cmp);
	printf("%d", paired[0].first);
}


bool solution(int n, vector<vector<int>> path, vector<vector<int>> order) {
	bool answer = true;





	return answer;
}