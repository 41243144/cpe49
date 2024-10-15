class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        import sys
        input = sys.stdin.read
        lines = input()

        result = ""
        count = 0

        for ch in lines:
            if ch == "\"":
                result += "``" if count % 2 == 0 else "''"
                count += 1
            else:
                result += ch
        print(result, end="")

if __name__ == "__main__":
    Solution()