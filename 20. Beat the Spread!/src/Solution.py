class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        # a+b = 40
        # a-b = 20
        # 2a = 60
        # a = 30
        # b = 10

        # a+b = 20
        # a-b = 40
        # 2a = 60
        # a = 30
        # b = -10

        # a = ( input1 + input2 ) / 2
        # input1 - a = b
        data_case_count = int(input())

        while data_case_count:
            data_case_count -= 1

            x, y = map(int, input().split())
            
            if (x + y) % 2 == 1:
                print("impossible")
                continue
            
            a = (x + y) // 2
            b = x - a

            if b < 0:
                print("impossible")
            else:
                print(f"{a} {b}")


if __name__ == "__main__":
    Solution()