#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    Solution() {
        this-> solve();
    }

    void solve() {

        // 讀取測資數量
        int n;
        cin >> n;

        while (n--) {
            //  讀取每行元素個數
            int length;
            cin >> length;

            vector<int> list(length);

            // 讀取元素
            for (int i = 0; i < length; i++) {
                cin >> list[i];
            }

            // 利用algorithm sort()排序
            sort(list.begin(), list.end());

            int mid = list[length / 2];
            cout << calculate(list, mid) << endl;

        }
    }

    int calculate(const vector<int>& list, int mid){
        /*
            計計算每個元素與中位數相差之和

            args:
                - list: <vector> int，陣列
                - mid: int，計算的值

            return 相差之和
        */
        int sum = 0;

        for(int val: list){
            if(val > mid){
                sum += val - mid;
            }else{
                sum += mid - val;
            }
        }

        return sum;
    }
};

int main() {
    Solution();
    return 0;
}