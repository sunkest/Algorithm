#include<iostream>
#include<algorithm>
using namespace std;
int N;
int dp[51][500001];
int h[51];
int main(void) {

	cin >> N;

	for(int i=1; i<=N; i++){
		cin >> h[i];
	}

	memset(dp, -1, sizeof(dp));

	int ans = D(0, 0);

}

int D(int idx, int diff) {
	if (diff > 500000 / 2)
		return -5;
	if (idx == N) {
		if (diff == 0)
			return 0;
		else
			return -5;
	}
	if (dp[idx][diff] != -1)
		return dp[idx][diff];

	dp[idx][diff] = D(idx + 1, diff);
	dp[idx][diff] = max(dp[idx][diff], D(idx + 1, diff + h[idx]));
	if (h[idx] > diff) {
		dp[idx][diff] = max(dp[idx][diff], diff + D(idx + 1, h[idx] - diff));
	}
	else {
		dp[idx][diff] = max(dp[idx][diff], h[idx] + D(idx + 1, diff - h[idx]));
	}
	
	return dp[idx][diff];
}

