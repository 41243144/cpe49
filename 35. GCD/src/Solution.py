class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        import math
        while True:
            
            n = int(input())
            result = 0

            if n == 0:
                break

            for i in range(1, n):
                for j in range(i + 1, n + 1):
                    result += math.gcd(i, j)

            print(result)

if __name__ == "__main__":
    Solution()