#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
	int answer = 0;
	vector<vector<int>> cams;
	sort(routes.begin(), routes.end());
		for (int i = 0; i < routes.size(); i++) {
			printf("%d,%d\n", routes[i][0], routes[i][1]);
		}
	for (vector<int> v : routes) {
		int a = min(v[0], v[1]); int b = max(v[0], v[1]);
		bool flag = false;
		
		for (int i = 0; i < cams.size(); i++) {

			int cam_a = cams[i][0]; int cam_b = cams[i][1];
			if (a > cam_b || b < cam_a) {	//겹치는 부분 없음
				continue;
			}
			else { //겹치는 부분 있음
				cams[i] = { max(a, cam_a), min(b, cam_b) };
				flag = true;
				break;		//겹치는 부분은 반드시 한번만 나옴 //cams끼리는 겹치는 부분이 없기때문
			}
			
		}
		if (!flag) { //겹치는 부분이 없었던 경우
			cams.push_back({ a,b });	//새로운 cam 추가
		}

	}
	answer = cams.size();
	return answer;
}

int main(void) {
	vector<vector<int>> routes = { {-7,0}, {-6,-4}, {-5,-3}, {-3,-1}, {-1,4}, {1,2}, {3,4} };
	printf("%d", solution(routes));
}