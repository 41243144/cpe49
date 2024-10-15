class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        count = 1
        while True:

            height, width = map(int, input().split())
            if height == width == 0:
                break

            result = [['0'] * width  for _ in range(height)]
            minesweeper = list()

            for _ in range(height):
                minesweeper.append(list(input()))
            
            for y in range(height):
                for x in range(width):
                    if minesweeper[y][x] == "*":
                        for add_y in range(-1, 2):
                            for add_x in range(-1, 2):
                                nx, ny = add_x + x, add_y + y
                                if 0 <= ny < height and 0 <= nx < width and result[ny][nx] != "*":
                                    result[ny][nx] = str(int(result[ny][nx]) + 1)

                        result[y][x] = '*'
            if count > 1:
                print()
            
            print(f"Field #{count}:")
            for row in result:
                print(''.join(map(str, row)))
            
            count += 1

if __name__ == "__main__":
    Solution()