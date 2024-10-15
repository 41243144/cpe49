class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case_count = int(input())
        count = 1

        while count <= data_case_count:
            # d = 2
            # a1 = start
            # an = end
            # an = a1 + (n - 1)* 2
            # an = a1 + 2n - 2
            # n = (-a1 + an + 2) / 2
            start = int(input())
            end = int(input())

            if start % 2 == 0:
                start += 1
            if end % 2 == 0:
                end -= 1

            n = (-start + end + 2) // 2

            s = (start + end) * n // 2

            print(f"Case {count}: {s}")
            count += 1


if __name__ == "__main__":
    Solution()