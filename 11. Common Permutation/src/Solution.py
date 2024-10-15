from collections import Counter
class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                counter1 = Counter(list(input().strip()))
                counter2 = Counter(list(input().strip()))

                counter = counter1 & counter2
                result = list()

                for char, times in counter.items():
                    result.extend([char] * times)
                
                result = sorted(result)

                print("".join(result))
            
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()