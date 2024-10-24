class Solution():
    def __init__(self) -> None:
        # 利用dict儲存已經出現過的狀態，初始化1為1步
        self.table = {1 : 1}
        self.main()
    
    def main(self) -> None:
        #資料讀取
        import sys
        input = sys.stdin.read
        data = list(map(int, input().split()))

        data_length = len(data)

        for index in range(0, data_length, 2):
            start = min(data[index], data[index + 1])
            end = max(data[index], data[index + 1])
            maxmium = 1

            for number in range(start, end + 1):
                
                maxmium = max(maxmium, self.process(number))

            print(f"{data[index]} {data[index + 1]} {maxmium}")

    
    # 計算number cycle length
    def process(self, number : int) -> int:
        if number in self.table:
            return self.table[number]
        if number % 2 == 1:
            self.table[number] = self.process(number * 3 + 1) + 1
        else:
            self.table[number] = self.process(number // 2) + 1
        return self.table[number]
    
if __name__ == "__main__":
    run = Solution()

