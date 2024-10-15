class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            a, b = map(int, input().split())
            if a == 0 and b == 0:
                break
            carry = 0
            count = 0

            while carry or (a and b):
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