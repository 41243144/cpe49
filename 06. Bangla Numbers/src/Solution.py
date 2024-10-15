class Solution:
    def __init__(self) -> None:
        self.case_number = 1
        self.main()

    def main(self):
        try:
            while True:
                number = int(input().strip())
                print(f"{self.case_number:4}. {self.to_bangla(number)}")
                self.case_number += 1
        except EOFError:
            pass

    def to_bangla(self, number):
        if number == 0:
            return "0"
        
        units = [
            (10000000, "kuti"),
            (100000, "lakh"),
            (1000, "hajar"),
            (100, "shata")
        ]
        
        result = list()

        if number >= 10000000:
            kuti_value = number // 10000000
            result.append(self.to_bangla(kuti_value))
            result.append("kuti")
            number %= 10000000

        for unit_val, unit_name in units:
            if number >= unit_val:
                result.append(f"{number // unit_val} {unit_name}")
                number %= unit_val

        if number > 0:
            result.append(str(number))

        return " ".join(result)


if __name__ == "__main__":
    Solution()
