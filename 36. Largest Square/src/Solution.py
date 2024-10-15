class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case = int(input())

        while data_case:
            data_case -= 1

            height, width, n = map(int, input().split())
            matrix = list()

            for _ in range(height):
                matrix.append(list(input()))

            print(f"{height} {width} {n}")
            
            for i in range(n):
                h, w = map(int, input().split())
                print(self.find_largest_square(matrix, h, w))
            
    def find_largest_square(self, matrix, h, w):
        count = 1

        ch = matrix[h][w]

        while True:
            if h - count < 0 or h + count >= len(matrix) or w - count < 0 or w + count >= len(matrix[0]):
                return 2 * count - 1
            
            for i in range(h - count, h + count + 1):
                for j in range(w - count, w + count + 1):
                    if matrix[i][j] != ch:
                        return 2 * count - 1
                
            count += 1

if __name__ == "__main__":
    Solution()