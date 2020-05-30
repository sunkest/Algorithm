#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;
vector<pair<int, int>> v;	//�ڹٿ����� pair ��� x, y �� �ΰ��ִ� Ŭ���� �ϳ� ������ ������Ǵµ�,
									//�׷��� �ϸ� sort�ϱⰡ ������.
bool cmp(const pair<int, int> &a, const pair<int, int> &b)
{
	return a.first > b.first;
}
int main(void) {
	//pair���� first�� ī��Ʈ, second�� ���ڷ�
	int n, c;
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;		//�̹� ���� ���Ϳ� �ִ��� Ȯ�� -> ���Դ� ������ Ȯ��
		bool flag = false;
		for (int j = 0; j < (int)v.size(); j++) {
			if (v[j].second == x) {			//���Դ� ���� ���
				flag = true;					//���Դٰ� ǥ��
				v[j].first = v[j].first + 1;	//count �ϳ� ����
				break;							//�ݺ��� �׸�
			}
		}
		if (!flag) {		//���Դ� ���̿��� ���
			v.push_back(make_pair(1, x));	//���Ϳ� �߰�
		}
	}	//�̰����� ���� ��ü �� �������� �ݺ�
	
	stable_sort(v.begin(), v.end(), cmp);	//���͸� count������ ����
													//C++�� sort()�Լ��� �� ����(heap sort) �˰��� ���
													// -> ���� ���� ������ ���� �ٲ� 
													// -> count�� ������� �������°� �������;� �ϴµ� ������ �ٲ�鼭 �ڼ��̸� �ȵ�
													//stable_sort()�� �պ� ����(merge sort) �˰��� ��� -> ���� ���߿��� ���� ������ �����
													//�ڹ��� Arrays.sort()�� merge sort ����ؼ� �Ű�Ƚᵵ��

	for (int i = 0; i < (int)v.size(); i++) {	//���� ���� ������ ���
		for (int j = 0; j < v[i].first; j++) {	//�ش� ���ڸ� count�� ��ŭ �ݺ��ؼ� ���
			printf("%d ", v[i].second);
		}
	}

}



