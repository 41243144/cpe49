class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case_count = int(input())
        count = 1

        while count <= data_case_count:
            a = int(input(), 2)
            b = int(input(), 2)

            # print(a, b)

            if self.gcd(a, b) == 1:
                print(f"Pair #{count}: Love is not all you need!")
            else:

                print(f"Pair #{count}: All you need is love!")

            count += 1

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

if __name__ == "__main__":
    Solution()