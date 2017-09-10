#include <iostream>
#include<algorithm>

using namespace std;

int maxValue(int N, int V, int m[], int w[], int s[]) {
  int dp[V+1];
  dp[0] = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= m[i]; j++) {
      for (int m = V; m >= w[i]; m--) {
        dp[m] = max(dp[m], dp[m - w[i]] + s[i]);
      }
    }
  }
  return dp[V];
}
int main()
{	
    int N, V;
    cin >> N >> V;
    int m[N], w[N], s[N];
    for (int i = 0; i < N; i++) {
      cin >> m[i] >> w[i] >> s[i];
    }
  	cout << maxValue(N, V, m, w, s) << endl;
  return 0;
}