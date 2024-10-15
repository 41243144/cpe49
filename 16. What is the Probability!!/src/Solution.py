class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        n = int(input())

            # p * (1 - p)^i-1 
            # 1 - (1 - p)^n
        while n:
            n -= 1
            player, p, i = map(float, input().split())

            if p == 0:
                print("0.0000")
                continue

            result = p * (1 - p) ** (i - 1) / (1 - (1 - p) ** player)

            print(f"{result:.4f}")



if __name__ == "__main__":
    Solution()