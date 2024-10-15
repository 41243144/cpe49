class Solution:
    def __init__(self) -> None:
        self.main()

    def main(self):
        n = int(input())
        input()

        while n:
            table = dict()
            total_trees = 0
            
            while True:
                try:
                    s = input().strip()
                except EOFError:
                    n -= 1
                    break

                if s == "":
                    n -= 1
                    break
                
                total_trees += 1
                if s in table:
                    table[s] += 1
                else:
                    table[s] = 1

            table_sorted = sorted(table.items(), key=lambda x: (x[0]))

            for key, value in table_sorted:
                percentage = (value / total_trees) * 100
                print(f"{key} {percentage:.4f}")

            if n > 0:
                print()

if __name__ == "__main__":
    Solution()
