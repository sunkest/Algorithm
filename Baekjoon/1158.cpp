#include <iostream>
#include <queue>
using namespace std;

int main(void) {
	int n, k;
	cin >> n >> k;

	queue<int> q;	//queue�� �ڹٿ��� ���� //�ڹٿ��� ����Ҷ��� Queue<Int> q = new LinkedList<Int>(); push()��� add(), pop()��� remove()
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}


	printf("<");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < k; j++) {
			if (j < k-1) {
				q.push(q.front());
				q.pop();
			}
			if (j == k-1) {
				if (q.size() == 1)
					printf("%d>", q.front());
				else
					printf("%d, ", q.front());
				q.pop();
			}
		}
	}

}