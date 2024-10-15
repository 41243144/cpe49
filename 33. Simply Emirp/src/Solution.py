class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        try:
            while True:
                number = input()
                number_reverse = int(number[::-1])
                number = int(number)

                number_status = self.is_prime(number)
                number_reverse_status = self.is_prime(number_reverse)

                if number_status:
                    if number_reverse_status and number != number_reverse:
                        print(f"{number} is emirp.")
                    else:
                        print(f"{number} is prime.")
                else:
                        print(f"{number} is not prime.")

        except EOFError:
            exit()
    def is_prime(self, number):
        if number <= 1:
            return False
        
        if number in [2, 3]:
            return True
        elif number % 2 == 0 or number % 3 == 0:
            return False
        
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        
        return True
        
if __name__ == "__main__":
    Solution()