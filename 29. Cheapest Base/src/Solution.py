class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case_count = int(input())
        count = 1

        search_table = self.create_search_table()
        
        while count <= data_case_count:
            table = list()

            for _ in range(4):
                table.extend(list(map(int, input().split())))
            
            search_table = dict(zip(search_table, table))

            print(f"Case {count}:")

            test_count = int(input())

            while test_count:
                test_count -= 1
                min_value = float("inf")

                result = [float("inf") for _ in range(37)]
                result.append(float("inf"))
                number = int(input())
                result_string = f"Cheapest base(s) for number {number}:"

                for base in range(2, 37):
                    base_number = self.base_transfer(number, base)
                    digit_sum = 0

                    for ch in base_number:
                        digit_sum += search_table[ch]
                    
                    min_value = min(min_value, digit_sum)
                
                    result[base] = digit_sum
                
                for i in range(2, 37):
                    if result[i] == min_value:
                        result_string += f" {i}"
                print(result_string)

            if count < data_case_count:
                print()

            count += 1

    def base_transfer(self, num, base):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        while num > 0:
            result = digits[num % base] + result
            num //= base
        
        return result if result else "0"
                    
    def create_search_table(self):
        table = list()

        for i in range(ord('9') - ord('0') + 1):
            table.append(chr(ord('0') + i))

        for i in range(ord('Z') - ord('A') + 1):
            table.append(chr(ord('A') + i))

        return table
if __name__ == "__main__":
    Solution()