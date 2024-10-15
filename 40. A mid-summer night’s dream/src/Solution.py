class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                n = int(input())
                data = list()

                for _ in range(n):
                    data.append(int(input()))
                
                data = sorted(data)
                length = len(data)

                if length % 2:
                    mid = data[length // 2]
                    print(f"{mid} {data.count(mid)} 1")

                else:
                    mid1 = data[length // 2 - 1]
                    mid2 = data[length // 2]
                    if mid1 == mid2:
                        print(f"{mid1} {data.count(mid1)} 1")
                    else:
                        print(f"{mid1} {data.count(mid1) + data.count(mid2)} {mid2 - mid1 + 1}")

        except EOFError:
            exit()
    
if __name__ == "__main__":
    Solution()