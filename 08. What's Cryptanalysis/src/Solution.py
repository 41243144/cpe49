class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            n = int(input())
            table = [0 for _ in range(26)]

            for _ in range(n):
                line = input().upper().strip()
                for i in line:
                    if "A" <= i <= "Z":
                            table[ord(i) - ord('A')] += 1
                
            for _ in range(26):
                max_value = max(table)
                if max_value == 0:
                    break
                index = table.index(max_value)
                table[index] = 0

                print(f"{chr(ord('A') + index)} {max_value}")

        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()