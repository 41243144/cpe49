class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                n = int(input())

                if n == 0:
                    break

                # top, north, west, east, south, buttom
                dice = [1, 2, 3, 4, 5, 6]

                for _ in range(n):
                    command = input()
                    if command == "north":
                        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
                    elif command == "south":
                        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
                    elif command == "east":
                        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
                    elif command == "west":
                        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
                
                print(dice[0])
        except ValueError:
            exit()

if __name__ == "__main__":
    Solution()