#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> weights;
vector<int> values;

int knapSackDynamic(int W) {

    vector<int> dp(W + 1, 0);

    for (int i = 0; i < n; i++)
        for (int w = W; w >= weights[i]; w--)
			  dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);

    return dp[W];
}


int main() {
    int W;
    cin >> n >> W;
    weights.reserve(n);
    values.reserve(n);
    for (int i = 0; i < n; ++i) {
        int w, v;
        cin >> w >> v;
        weights.push_back(w);
        values.push_back(v);
    }
	cout << knapSackDynamic(W) << '\n'; 
}