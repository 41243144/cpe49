#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    Solution() {
        table[1] = 1;
        this->main();
    }

private:
    unordered_map<int, int> table;

    void main() {
        int a, b;

        while (cin >> a >> b) {
            int i = min(a, b);
            int j = max(a, b);

            int maxCycleLength = 0;

            for (int k = i; k <= j; ++k) {
                maxCycleLength = max(maxCycleLength, process(k));
            }

            cout << a << ' ' << b << ' ' << maxCycleLength << endl;
        }
    }

    int process(int number) {
        if (table.find(number) != table.end()) {
            return table[number];
        }

        int result;
        if (number % 2 == 0) {
            result = process(number / 2) + 1;
        }
        else {
            result = process(number * 3 + 1) + 1;
        }
        table[number] = result;
        return result;
    }
};

int main() {
    Solution();
    return 0;
}
