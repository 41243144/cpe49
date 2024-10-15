class Solution():
    # 當類別建構執行main() function
    def __init__(self) -> None:
        self.main()
    def main(self):
        # 當出現EOF例外時結束程式執行
        try:
            while True:
                # 被除數 除數讀入
                dividend, divisor = map(int, input().split())
                # 紀錄被整除的數字
                record = list()
                record.append(dividend)

                # 若被除數為1時代表不可能被整除到，所以輸出Boring並跳到下一筆測資
                if divisor == 1:
                    print("Boring!")
                    continue
                
                # 循環直到被除數=1 (除數/除數)若可整除，不能整除提前離開
                while dividend > 1:
                    if dividend % divisor:
                        print("Boring!")
                        break
                    dividend //= divisor
                    # 添加紀錄
                    record.append(dividend)
                
                # 輸出格式中間要空格
                if dividend == 1:
                    print(" ".join(map(str, record)))
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()