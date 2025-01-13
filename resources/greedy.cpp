#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> weights;
vector<int> values;

int knapsackGreedy(int W) {
    struct Item {
        int value, weight;
        double ratio;
        bool operator < (const Item& other) const {
            return this->ratio > other.ratio;
        }
    };

    vector<Item> items(n);
    for (int i = 0; i < n; i++)
        items[i] = {values[i], weights[i], (double)values[i] / weights[i]};

    sort(items.begin(), items.end());

    int totalValue = 0;
    for (int i = 0; i < n && W > 0; i++)
        if (W >= items[i].weight) {
            W -= items[i].weight;
            totalValue += items[i].value;
        }

    return totalValue;
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
	cout << knapsackGreedy(W) << '\n'; 
}