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

	sort(treeX.begin(), treeX.end(), cmpByX);		//x좌표로 소팅
	sort(treeY.begin(), treeY.end(), cmpByY);		//y좌표로 소팅

	int p;
	scanf("%d", &p);
	for (int i = 0; i < p; i++) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		int count = 0;
		//이진 탐색으로 시간 줄임
		//아래의 upper_bound, lower_bound는 자바에서는 Arrays.BinarySearch() 사용하면 됨
		
		//좌측 변
		count += upper_bound(treeX.begin(), treeX.end(), make_pair(x1, y2), cmpByX)	//upper_bound는 마지막 원소부터 찾다가 원하는 값이 시작되기 직전의 위치를 알아내는 함수
					- lower_bound(treeX.begin(), treeX.end(), make_pair(x1, y1), cmpByX);	//lower_bound는 첫 원소부터 찾다가 원하는 값 이상이 되기 시작하는 위치를 알아내는 함수
		//우측 변
		count += upper_bound(treeX.begin(), treeX.end(), make_pair(x2, y2), cmpByX)
					- lower_bound(treeX.begin(), treeX.end(), make_pair(x2, y1), cmpByX);
		//하단 변
		count += upper_bound(treeY.begin(), treeY.end(), make_pair(x2-1, y1), cmpByY)	//+1, -1은 꼭지첨 처리
					- lower_bound(treeY.begin(), treeY.end(), make_pair(x1+1, y1), cmpByY);
		//상단 변
		count += upper_bound(treeY.begin(), treeY.end(), make_pair(x2-1, y2), cmpByY)
					- lower_bound(treeY.begin(), treeY.end(), make_pair(x1+1, y2), cmpByY);
		
		printf("%d\n", count);
	}







}