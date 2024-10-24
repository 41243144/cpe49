#include <iostream>

using namespace std;

class Solution{
public:
    Solution(){
        this -> solve();
    }
    void solve(void){
        long long a, b;
        while(cin >> a >> b){
            if(a > b){
                cout << a - b << endl;
            }else{
                cout << b - a << endl;
            }
        }
    }
};


int main(){
    Solution();
    return 0;
}