class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                n = int(input())
                
                print(max(self.cola(n), self.cola(n + 1) - 1))

        except EOFError:
            exit()

    def cola(self, number):
        total = number
        empty_bottle = number

        while empty_bottle >= 3:
            new_bottle, empty_bottle = divmod(empty_bottle, 3)
            total += new_bottle

            empty_bottle += new_bottle

        return total
    
if __name__ == "__main__":
    Solution()