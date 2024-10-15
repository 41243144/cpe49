class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                check_in, target = map(int, input().split())

                count = check_in

                while check_in < target:
                    count += 1
                    check_in += count
                print(count)
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()