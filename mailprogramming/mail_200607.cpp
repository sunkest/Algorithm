#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	vector<int> input = { 2,4,-2,-3,8 };
	int cur_max = input[0];
	int cur_sum = input[0];
	for (int i = 1; i < input.size(); i++) {
		cur_sum = max(cur_sum + input[i], input[i]);
		cur_max = max(cur_max, cur_sum);
	}
	printf("%d", cur_max);
}