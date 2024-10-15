class Solution():
    def __init__(self) -> None:
        self.main()
    
    def main(self):
        try:
            lines = list()
            while True:
                line = list(input().rstrip('\t'))

                if not line:
                    continue

                lines.append(line)
                
        except EOFError:
            Fg = True

            while Fg:
                Fg = False
                s = ""
                for i in range(len(lines) -1, -1, -1):
                    if lines[i]:
                        ch = lines[i].pop(0)
                        Fg = True
                        s += ch
                    else:
                        s += " "
                if Fg:
                    print(s)
if __name__ == "__main__":
    Solution()