#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool cmpByX(const pair<int,int> &A, const pair<int,int> &B) {
	if (A.first != B.first) return A.first < B.first; 
	else return A.second < B.second;
}
bool cmpByY(const pair<int, int> &A, const pair<int, int> &B) {
	if (A.second != B.second) return A.second < B.second;
	else return A.first < B.first;
}
int main(void) {
	int n;
	scanf("%d", &n);
	vector<pair<int, int>> treeX, treeY;
	for (int i = 0; i < n; i++) {
		int x, y;
		scanf("%d%d", &x, &y);
		treeX.push_back(make_pair(x, y));
		treeY.push_back(make_pair(x, y));
	}

	sort(treeX.begin(), treeX.end(), cmpByX);		//x��ǥ�� ����
	sort(treeY.begin(), treeY.end(), cmpByY);		//y��ǥ�� ����

	int p;
	scanf("%d", &p);
	for (int i = 0; i < p; i++) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		int count = 0;
		//���� Ž������ �ð� ����
		//�Ʒ��� upper_bound, lower_bound�� �ڹٿ����� Arrays.BinarySearch() ����ϸ� ��
		
		//���� ��
		count += upper_bound(treeX.begin(), treeX.end(), make_pair(x1, y2), cmpByX)	//upper_bound�� ������ ���Һ��� ã�ٰ� ���ϴ� ���� ���۵Ǳ� ������ ��ġ�� �˾Ƴ��� �Լ�
					- lower_bound(treeX.begin(), treeX.end(), make_pair(x1, y1), cmpByX);	//lower_bound�� ù ���Һ��� ã�ٰ� ���ϴ� �� �̻��� �Ǳ� �����ϴ� ��ġ�� �˾Ƴ��� �Լ�
		//���� ��
		count += upper_bound(treeX.begin(), treeX.end(), make_pair(x2, y2), cmpByX)
					- lower_bound(treeX.begin(), treeX.end(), make_pair(x2, y1), cmpByX);
		//�ϴ� ��
		count += upper_bound(treeY.begin(), treeY.end(), make_pair(x2-1, y1), cmpByY)	//+1, -1�� ����÷ ó��
					- lower_bound(treeY.begin(), treeY.end(), make_pair(x1+1, y1), cmpByY);
		//��� ��
		count += upper_bound(treeY.begin(), treeY.end(), make_pair(x2-1, y2), cmpByY)
					- lower_bound(treeY.begin(), treeY.end(), make_pair(x1+1, y2), cmpByY);
		
		printf("%d\n", count);
	}







}