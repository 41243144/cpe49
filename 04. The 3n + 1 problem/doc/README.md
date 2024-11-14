# 04. The 3n + 1 problem

## 題目大意
---

#### 考慮以下的演算法：
1. 輸入 n
2. 印出 n
3. 如果 n = 1 結束
4. 如果 n 是奇數 那麼 n=3*n+1
5. 否則 n=n/2
6. GOTO 2

#### 例如輸入 `22`, 得到的數列： `22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1` 

##### 據推測此演算法對任何整數而言會終止 (當列印出 1 的時候)。雖然此演算法很簡單，但以上的推測是否真實卻無法知道。然而對所有的n ( 0 < n < 1,000,000 )來說，以上的推測已經被驗證是正確的。 

##### 給一個輸入 n ,透過以上的演算法我們可以得到一個數列（1作為結尾）。此數列的長度稱為n的cycle-length。上面提到的例子, 22 的 cycle length為 16. 

##### 問題來了：對任2個整數i，j我們想要知道介於i，j（包含i，j）之間的數所產生的數列中最大的 cycle length 是多少。
---

##### 輸入說明: 輸入可能包含了好幾列測試資料，每一列有一對整數資料 i，j 。 0< i，j < `1,000,000`

----

##### 輸出說明: 對每一對輸入 i , j 你應該要輸出 i, j 和介於 i, j 之間的數所產生的數列中最大的 cycle length。

---

##### 範例輸入:
```
1 10
10 1
100 200
201 210
900 1000
```

##### 範例輸出:
```
1 10 20
10 1 20
100 200 125
201 210 89
900 1000 174
```

---

## 解題說明
---
#### 因為在解3n + 1 problem可能會有許多重複的計算，為提升效率，我將建立一個儲存格存放已經計算過的數據

#### 程式講解(Python)

```python
class Solution():
    def __init__(self) -> None:
        # 利用dict儲存已經出現過的狀態，初始化1為1步
        self.table = {1 : 1}
        self.main()
```
1. 資料讀取及處理
```python
# 這裡覆蓋原本input()，原本input()是讀取一行，這裡變更為讀取整個檔案
import sys
input = sys.stdin.read

# 將每一個元素轉換成int後轉為list形式儲存
data = list(map(int, input().split()))
```
2. 迴圈運作
```python
# 取得list長度
data_length = len(data)

# 等於c++for(int index; index < data_length; index + 2)
for index in range(0, data_length, 2):
    # 取得較小數字設定為start，較大的就為end
    start = min(data[index], data[index + 1])
    end = max(data[index], data[index + 1])
    # 初始化最大值為1

    maxmium = 1

    for number in range(start, end + 1):
        # 執行process function
        # 取得最大值
        maxmium = max(maxmium, self.process(number))

    # print 結果
    print(f"{data[index]} {data[index + 1]} {maxmium}")
```
```python
# process有一個參數number，反回型態為int
def process(self, number : int) -> int:
    # 若目標已經計算過則直接返回，儲存到dict中
    if number in self.table:
        return self.table[number]
    # 若為竒數執行 3n+1 ，並將計數次數+1，儲存到dict中
    if number % 2 == 1:
        self.table[number] = self.process(number * 3 + 1) + 1
    # 若為偶數執行 n / 2 ，並將計數次數+1
    else:
        self.table[number] = self.process(number // 2) + 1

    return self.table[number]
```
#### 程式講解(C++)
1. 凾式庫引入
```c++
#include <iostream>
#include <unordered_map>
#include <algorithm>
```

2. 類別初始化
```c++
class Solution {
public:
    Solution() {
        table[1] = 1;
        this->main();
    }
```
3. 讀進資料並且記錄範圍最大值並輸出
```c++
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
```
---
```c++
int process(int number) {
    /*
        不斷遞迴直到1或是途中找到已經有紀錄的提早返回
    */
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
```
---
#### 主程式執行區
```c++
int main() {
    Solution();
    return 0;
}
```
---

##### By. wenwen
##### 參考資料:[高中生程式解題系統](https://zerojudge.tw/)