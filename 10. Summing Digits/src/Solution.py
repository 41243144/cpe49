class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            number = int(input())

            if number == 0:
                break

            while number >= 10:
                number = self.summing_digit(number)
            print(number)

    def summing_digit(self, number):
        sum = 0
        while number:
            sum += number % 10
            number //= 10
        return sum

if __name__ == "__main__":
    Solution()