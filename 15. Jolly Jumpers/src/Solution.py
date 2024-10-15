class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        import sys
        input = sys.stdin.read

        lines = input().strip().split('\n')

        for line in lines:
            data = list(map(int, line.split()))
            definition = list()

            if data[0] == 1:
                print("Jolly")
                continue
            else:
                length = data.pop(0)
                for i in range(1, length):
                    definition.append(abs(data[i] - data[i-1]))
                
            jully = [i for i in range(1, length)]
            definition.sort()

            if jully == definition:
                print("Jolly")
            else:
                print("Not jolly")
if __name__ == "__main__":
    Solution()