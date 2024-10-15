class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            number = input()
            if number == '0':
                break

            result = self.calculate_9_degree(number)

            if result == -1:
                print(f"{number} is not a multiple of 9.")
            else:
                print(f"{number} is a multiple of 9 and has 9-degree {result}.")

    def calculate_9_degree(self, number):
        degree = 0
        if number == '9':
            return 1
        while len(number) > 1:
            number = str(sum(int(x) for x in number))
            degree += 1


        if int(number) % 9 == 0:
            return degree
        else:
            return -1
if __name__ == "__main__":
    Solution()