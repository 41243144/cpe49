class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            x_max, y_max = map(int, input().split())
            direction = ["N", "E", "S", "W"]
            record = set()

            while True:
                init_x, init_y, init_dire = input().split()
                init_x, init_y = int(init_x), int(init_y)
                count = direction.index(init_dire)
                commands = input()
                lost = False

                for command in commands:
                    if command == "R":
                        count = (count + 1) % 4
                        init_dire = direction[count]

                    elif command == "L":
                        count = (count - 1) % 4
                        init_dire = direction[count]

                    else:
                        if (init_x, init_y, init_dire) in record:
                            continue
                        elif init_dire == "N" and init_y + 1 <= y_max:
                            init_y += 1

                        elif init_dire == "S" and init_y - 1 >= 0:
                            init_y -= 1

                        elif init_dire == "E" and init_x + 1 <= x_max:
                            init_x += 1

                        elif init_dire == "W" and init_x - 1 >= 0:
                            init_x -= 1
                        else:
                            lost = True
                            record.add((init_x, init_y, init_dire))
                            break
                
                if lost:
                    print(f"{init_x} {init_y} {init_dire} LOST")
                else:
                    print(f"{init_x} {init_y} {init_dire}")
                
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()