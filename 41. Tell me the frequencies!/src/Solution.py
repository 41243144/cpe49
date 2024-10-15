class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        import sys
        input = sys.stdin.read
        
        lines = input().splitlines()

        length = len(lines)

        for index, line in enumerate(lines):
            table = dict()

            for ch in line:
                ch_ascii = ord(ch)
                if 32 <= ch_ascii <= 128:
                    if ch_ascii not in table:
                        table[ch_ascii] = 1
                    else:
                        table[ch_ascii] += 1
            
            table = sorted(table.items(), key= lambda x: self.table_sort(x))

            for key, value in table:
                print(f"{key} {value}")

            if index + 1 < length:
                print()

    def table_sort(self, key):
        return  (key[1], -key[0]) 
if __name__ == "__main__":
    Solution()