
// Heuristic solution for the Knapsack problem
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int weight, value;
    double ratio;
};

bool compare(Item a, Item b) {
    return a.ratio > b.ratio;
}

int knapsack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector<Item> items;
    for (int i = 0; i < n; i++) {
        items.push_back({wt[i], val[i], (double)val[i] / wt[i]});
    }
    sort(items.begin(), items.end(), compare);

    int totalValue = 0;
    for (auto& item : items) {
        if (W >= item.weight) {
            W -= item.weight;
            totalValue += item.value;
        } else {
            totalValue += item.ratio * W;
            break;
        }
    }
    return totalValue;
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
