class Solution():
    # 當類別建構執行main() function
    def __init__(self) -> None:
        self.main()


    def main(self):
        # 測資數量
        data_count = int(input())

        while data_count:
            # 讀進輸入資料
            data = list(map(int, input().split())) 
            # pop(0)因為第一筆是數量
            data.pop(0)
            data_length = len(data)
            median = data_length // 2
            data.sort()

            if data_length % 2:
                # 因為奇數，所以判斷中位數 跟中位數 + 1
                result = min(self.result_return(data, data[median]), self.result_return(data, data[median + 1]))
                print(result)
            else:
                print(self.result_return(data, data[median]))

            data_count -= 1

    def result_return(self, data: list, median: int) -> int:
        '''
            回傳中位數跟每個元素相減之結果
        '''
        # 初始化結果
        result = 0

        # 將每個元素跟中位數相減
        for element in data:
            result += abs(median - element)

        return result


if __name__  == "__main__":
    Solution()