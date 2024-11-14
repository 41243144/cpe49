class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            # 讀取a, b
            a, b = map(int, input().split())
            # 若a b都為0代表輸入結束
            if a == 0 and b == 0:
                break
            # 初始化進未及計數為0
            carry = 0
            count = 0

            # 若a b都不為0就繼續更新carry 為 a b個別取10餘數並 +上 carry 之後除10，若carry 為1代表進位則count + 1
            while a or b:
                carry = (a % 10 + b % 10 + carry) // 10

                if carry:
                    count += 1
                
                a //= 10
                b //= 10

            if count == 0:
                print("No carry operation.")
            elif count == 1:
                print(f"{count} carry operation.")
            else:
                print(f"{count} carry operations.")
                

if __name__ == "__main__":
    Solution()