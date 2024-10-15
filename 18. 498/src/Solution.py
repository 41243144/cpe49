class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:    
            while True:
                x = int(input())
                polynomial = list(map(int, input().split()))
                length = len(polynomial)
                result = 0
                power = 0

                if length == 1:
                    print(0)
                    continue

                for i in range(length - 2, -1, -1):
                    result += x ** power * polynomial[i] * (length - i - 1)
                    power += 1
                
                print(result)

        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()