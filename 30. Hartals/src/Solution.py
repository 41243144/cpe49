class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case_count = int(input())
        while data_case_count:
            data_case_count -= 1

            days = int(input())
            n = int(input())
            result = set()

            for _ in range(n):
                d = int(input())
                for h in range(d, days + 1, d):
                    if h % 7 not in [0, 6]:
                        result.add(h)

            print(len(result))

if __name__ == "__main__":
    Solution()