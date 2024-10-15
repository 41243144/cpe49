class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        data_case_count = int(input())
        count = 1

        while count <= data_case_count:
            _, n = input().split('=')
            n = int(n)

            matrix = list()

            for _ in range(n):
                line = list(map(int, input().split()))
                matrix.extend(line)
 
            if matrix == matrix[::-1] and -1 not in matrix:
                print(f"Test #{count}: Symmetric.")
            else:
                print(f"Test #{count}: Non-symmetric.")
            
            count += 1

if __name__ == "__main__":
    Solution()