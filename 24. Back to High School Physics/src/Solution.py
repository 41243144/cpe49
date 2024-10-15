class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                v, t = map(int, input().split())

                print(v * t * 2)
                
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()