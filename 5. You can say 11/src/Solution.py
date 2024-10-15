class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            number = number1 = int(input())
            pds = 0 # phase diffference synthesis
            if number == 0:
                break
            
            while number:
                pds += number % 10
                number //= 10
                pds -= number % 10
                number //=10
            
            if abs(pds) % 11 == 0:
                print(f"{number1} is a multiple of 11.")
            else:
                print(f"{number1} is not a multiple of 11.")

if __name__ == "__main__":
    Solution()