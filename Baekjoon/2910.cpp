#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;
vector<pair<int, int>> v;	//자바에서는 pair 대신 x, y 값 두개있는 클래스 하나 간단히 만들어쓰면되는데,
									//그렇게 하면 sort하기가 불편함.
bool cmp(const pair<int, int> &a, const pair<int, int> &b)
{
	return a.first > b.first;
}
int main(void) {
	//pair에는 first를 카운트, second를 숫자로
	int n, c;
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;		//이번 값이 벡터에 있는지 확인 -> 나왔던 값인지 확인
		bool flag = false;
		for (int j = 0; j < (int)v.size(); j++) {
			if (v[j].second == x) {			//나왔던 값인 경우
				flag = true;					//나왔다고 표시
				v[j].first = v[j].first + 1;	//count 하나 증가
				break;							//반복문 그만
			}
		}
		if (!flag) {		//나왔던 값이였던 경우
			v.push_back(make_pair(1, x));	//벡터에 추가
		}
	}	//이과정을 수열 전체 다 볼때까지 반복
	
	stable_sort(v.begin(), v.end(), cmp);	//벡터를 count순으로 정렬
													//C++의 sort()함수는 힙 정렬(heap sort) 알고리즘 사용
													// -> 정렬 도중 순서가 마구 바뀜 
													// -> count가 같은경우 먼저나온게 먼저나와야 하는데 순서가 바뀌면서 뒤섞이면 안됨
													//stable_sort()는 합병 정렬(merge sort) 알고리즘 사용 -> 정렬 도중에도 들어온 순서가 보장됨
													//자바의 Arrays.sort()는 merge sort 사용해서 신경안써도됨

	for (int i = 0; i < (int)v.size(); i++) {	//벡터 내의 내용을 출력
		for (int j = 0; j < v[i].first; j++) {	//해당 숫자를 count된 만큼 반복해서 출력
			printf("%d ", v[i].second);
		}
	}

}



