class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            n, target = map(int, input().split())

            if n == target == 0:
                print("0 0")
                break

            array = list()

            for _ in range(n):
                array.append(int(input()))

            array = sorted(array, key=lambda x: self.sort_key(x, target))

            print(f"{n} {target}")
            print("\n".join(map(str, array)))

    def sort_key(self, x, target):
        if x < 0:
            mod = -(-x % target)
        else:
            mod = x % target
        if x % 2 == 0:
            return (mod, 0, x)
        else:
            return (mod, -1, -x)

if __name__ == "__main__":
    Solution()