# include <iostream>
using namespace std;

class Solution{
public:
    Solution(){
        this -> solve();
    }

private:
    void solve(){
        int a, b;

        while (true)
        {
            cin >> a >> b;

            if(a == 0 && b == 0) break;

            // 初始化進未及計數為0
            int c = 0;
            int times = 0;

            // 若a b都不為0就繼續更新carry 為 a b個別取10餘數並 +上 carry 之後除10，若carry 為1代表進位則count + 1
            while (a || b){
                int temp = a % 10 + b % 10 + c;
                c = temp / 10;
                if(c == 1) times ++;
                a /= 10;
                b /= 10;
            }

            if(times == 0){
                cout << "No carry operation." << endl;
            }else if(times == 1){
                cout << "1 carry operation." << endl;
            }else{
                cout << times << " carry operations." << endl;
            }
        }
        
    }
};

int main(){
    Solution();
    return 0;
}