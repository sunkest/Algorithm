#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g;
bool c[101] = { false };
int a = 0;

void dfs(int n) {
	a++;
	c[n] = true;
	
	for (int i = 0; i < g[n].size(); i++) {
		if (!c[g[n][i]]) dfs(g[n][i]);
	}
	return;
}


int main(void) {

	int pc, link;
	cin >> pc >> link;

	g.resize(pc + 1);

	for (int i = 0; i < link; i++) {
		int a, b;
		cin >> a >> b;
		g[a].push_back(b);
		g[b].push_back(a);
	}
	

	
	dfs(1);

	printf("%d", a-1);	//1¹ø Á¦¿Ü
}