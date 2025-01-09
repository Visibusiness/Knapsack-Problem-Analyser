
// Brute-force solution for the Knapsack problem
#include <iostream>
#include <vector>
using namespace std;

int knapsack(int W, vector<int>& wt, vector<int>& val, int n) {
    if (n == 0 || W == 0)
        return 0;
    if (wt[n-1] > W)
        return knapsack(W, wt, val, n-1);
    return max(val[n-1] + knapsack(W - wt[n-1], wt, val, n-1),
               knapsack(W, wt, val, n-1));
}

int main() {
    int n, W;
    cin >> n >> W;
    vector<int> wt(n), val(n);
    for (int i = 0; i < n; ++i) {
        cin >> wt[i] >> val[i];
    }
    cout << knapsack(W, wt, val, n) << endl;
    return 0;
}
