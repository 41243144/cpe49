class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        import math
        try:
            while True:
                s, degree, degree_min = input().split()

                r = 6440 + int(s)

                if degree_min == "min":
                    degree = int(degree) / 60
                else:
                    degree = int(degree)

                radians = math.radians(degree)

                arc = r * radians

                chord = 2 * r * math.sin(radians / 2)

                print(f"{arc:.6f} {chord:.6f}")
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()