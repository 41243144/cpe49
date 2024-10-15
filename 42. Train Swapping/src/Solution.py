class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case = int(input())

        while data_case:
            input()
            data_case -= 1
            data = list(map(int, input().split()))
            data_length = len(data)
            count = 0

            for i in range(data_length - 1):
                for j in range(i + 1, data_length):
                    if data[i] > data[j]:
                        data[i], data[j] = data[j], data[i]
                        count += 1
            print(f"Optimal train swapping takes {count} swaps.")

if __name__ == "__main__":
    Solution()