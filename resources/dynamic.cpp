#include <iostream>

#define MAX(a, b) (a > b ? a : b)

using namespace std;

int v[10000];


int main()
{
    int N, g, w, p;
    cin >> N >> g;
    for (int n = 0; n < N; n++) {
        cin >> w >> p;
        for (int i = g; i >= w && i >= 1; i--)
            v[i] = MAX(v[i], v[i - w] + p);
    }
    cout << v[g] << endl;
}