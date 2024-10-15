class Solution():
    def __init__(self) -> None:
        self.main()
    def main(self):
        try:
            while True:
                a, b = map(int, input().split())
                print(abs(a - b))
        except EOFError:
            exit()


if __name__ == "__main__":
    Solution()