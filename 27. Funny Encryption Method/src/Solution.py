class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case = int(input())

        while data_case:
            
            data_case -= 1
            n = int(input())

            b1 = str(bin(n))[2:].count('1')

            b2 = str(bin(int(str(n), 16)))[2:].count('1')

            print(f"{b1} {b2}")

if __name__ == "__main__":
    Solution()