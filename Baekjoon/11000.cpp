#include <iostream>
#include <algorithm>
#include <queue>
#include <functional>
#include <vector>
using namespace std;

vector<pair<int, int>> v;	//���� ������ ����
priority_queue<int, vector<int>, greater<int>> q;	//���ǽǺ��� ����ð� �ִ� �켱����ť

int main(void) {
	int n;
	cin >> n;
	v.resize(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i].first >> v[i].second;
	}
	sort(v.begin(), v.end());	//�Է´ٹ����� ���� ���۽ð� �������� ���� ����

	//ù��°���� ���� �ֱ�
	q.push(v[0].second);

	for (int i = 1; i < v.size(); i++) {		//���� �ϳ��� Ȯ��
												//�켱����ť�� top(���� ���� ������ ���� �ð�)�� i��° ���� ���۽ð� ��
		if (v[i].first >= q.top()) {		//���廡�������� ���� ���� �ʰ� �����ϴ� ���
			q.pop();	//pop�ϰ�
			q.push(v[i].second);	//�� ���� ����ð� push
		}
		else q.push(v[i].second);	//��밡���� ���ǽ� ���� ��� �� ���ǽǷ� push
	}

	printf("%d\n", q.size());	//�������� ť ����� ���ǽ� ��

}