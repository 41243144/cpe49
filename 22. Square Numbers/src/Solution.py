class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        import math
        while True:

            start, end = map(int, input().split())

            if start == end == 0:
                break

            start = math.ceil(math.sqrt(start))
            end = math.floor(math.sqrt(end))

            print(end - start + 1)

if __name__ == "__main__":
    Solution()