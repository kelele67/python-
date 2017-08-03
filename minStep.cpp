#include <iostream>
#include <vector>
#include <climits>
#include <cmath>
#include <algorithm>

using namespace std;

// steps[i]表示到达i号石板所需的最小步数
// 初始化为steps容器为INT_MAX。从序号N的石板开始逐个遍历，若steps[i]为INT_MAX，表示该点不可到达，直接开始下次循环。
// 若steps[i]不为INT_MAX，表示该点可以到达，下面求解编号i的约数，进行动态规划。
// 动态规划的转移方程为
// steps[i+j] = min(steps[i]+1, steps[i+j]) 
int main() {
	int N, M;
	while (cin >> N >> M) {
		vector<int> steps(M+1, INT_MAX);
		steps[N] = 0;
		for (int i = N; i <= M; i++) {
			if (steps[i] == INT_MAX) {
				continue;
			}
			for (int j = 2; (j*j) <= i; j++) {
				if (i % j == 0) {
					if (i + j <= M) {
						steps[i+j] = min(steps[i]+1, steps[i+j]);
					}
					if (i + (i / j) <= M) {
						steps[i+(i/j)] = min(steps[i]+1, steps[i+(i/j)]);
					}
				}
			}
		}
		if (steps[M] == INT_MAX) {
			steps[M] = -1;
		}
		cout << steps[M] << endl;
	}
	return 0;
}