class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        while True:
            decimal = int(input())

            if decimal == 0:
                break
                
            binary = str(bin(decimal))[2:]
            count = binary.count('1')
            print(f"The parity of {binary} is {count} (mod 2).")
            

if __name__ == "__main__":
    Solution()