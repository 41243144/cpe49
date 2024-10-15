class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            n = int(input())
            hash_table = dict()
            countries = list()
            
            for _ in range(n):
                country = list(input().split())[0]
                if country in hash_table:
                    hash_table[country] += 1
                else:
                    countries.append(country)
                    hash_table[country] = 1

            countries = sorted(countries)

            for country in countries:
                print(f"{country} {hash_table[country]}")
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()