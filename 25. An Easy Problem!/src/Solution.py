class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):

        try:
            while True:
                line = input().strip().lstrip("+-")
                min_base = 1
                sum = 0

                for digit in line:
                    if ord("0") <= ord(digit) <= ord("9"):
                        temp = ord(digit) - ord("0")
                    elif ord("A") <= ord(digit) <= ord("Z"):
                        temp = ord(digit) - ord("A") + 10
                    elif ord("a") <= ord(digit) <= ord("z"):
                        temp = ord(digit) - ord("a") + 36
                    else:
                        continue
                
                    sum += temp
                    min_base = max(min_base, temp)

                while min_base < 63:
                    if sum % min_base == 0:
                        print(min_base + 1)
                        break
                    min_base += 1

                if min_base == 63:
                    print("such number is impossible!")
                

        except EOFError:
            exit()


if __name__ == "__main__":
    Solution()