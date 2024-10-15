class Solution():
    def __init__(self) -> None:
        self.MAX_NUMBER = 100_000_000
        self.table = list()
        self.create_fac_table()
        self.main()

    def main(self):
        data_case_count = int(input())

        while data_case_count:

            data_case_count -= 1
            
            target = int(input())
            result_string = f"{target} = "
            result = list()

            for number in reversed(self.table):
                if result:
                    if number <= target:
                        target -= number
                        result.append('1')
                    else:
                        result.append('0')
                else:
                    if number <= target:
                        target -= number
                        result.append('1')
            
            result_string += "".join(result)
            print(f"{result_string} (fib)")


        
    def create_fac_table(self):
        self.table.extend([1, 2])

        while self.table[-1] < self.MAX_NUMBER:
            self.table.append(self.table[-1] + self.table[-2])

if __name__ == "__main__":
    Solution()