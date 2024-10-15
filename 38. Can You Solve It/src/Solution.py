class Solution:
    def __init__(self):
        self.main()

    def main(self):
        n = int(input())
        count = 0
        while count < n:
            count += 1
            x1, y1, x2, y2 = map(int, input().split())

            distance = (x2 + y2) * (x2 + y2 + 1) // 2 + x2 - (x1 + y1) * (x1 + y1 + 1) // 2 - x1
            print(f"Case {count}: {distance}")


if __name__ == "__main__":
    Solution()
