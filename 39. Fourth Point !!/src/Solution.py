class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:

                x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())

                result_x, result_y = 0, 0

                if x1 == x3 and y1 == y3:
                    result_x = x2 + x4 - x1
                    result_y = y2 + y4 - y1

                elif x1 == x4 and y1 == y4:
                    result_x = x2 + x3 - x1
                    result_y = y2 + y3 - y1

                elif x2 == x3 and y2 == y3:
                    result_x = x1 + x4 - x2
                    result_y = y1 + y4 - y2

                elif x2 == x4 and y2 == y4:
                    result_x = x1 + x3 - x2
                    result_y = y1 + y3 - y2

                print(f"{result_x:.3f} {result_y:.3f}")
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()