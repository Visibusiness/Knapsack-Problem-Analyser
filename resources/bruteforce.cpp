#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> weights;
vector<int> values;

int knapSackBacktracking(int W, int i) {

    if (W <= 0 || i >= n)
        return 0;

	int itemNotIncluded = knapSackBacktracking(W, i + 1);
	if (W < weights[i])
		return itemNotIncluded;

	int itemIncluded = values[i] + knapSackBacktracking(W - weights[i], i + 1);
	return max(itemNotIncluded, itemIncluded);
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
	cout << knapSackBacktracking(W, 0) << '\n'; 
}