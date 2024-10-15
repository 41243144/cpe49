class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            case_count = 0
            while True:
                case_count += 1

                i = input()
                if not i:
                    input()
                data = list(map(int, input().split()))
                length = len(data)

                if length in [1, 2]:
                    print(f"Case #{case_count}: It is a B2-Sequence.")
                    print()
                    continue

                count = data[1] - data[0]
                is_b2 = True

                for i in range(1, len(data)-1):
                    if data[i] - data[i-1] == count:
                        count += 1
                    else:
                        is_b2 = False
                        break
                
                if is_b2:
                    print(f"Case #{case_count}: It is a B2-Sequence.")
                else:
                    print(f"Case #{case_count}: It is not a B2-Sequence.")
                    
                print()

        except EOFError:
            exit()
if __name__ == "__main__":
    Solution()