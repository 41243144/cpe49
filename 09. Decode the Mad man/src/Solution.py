class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        keyboard = r"`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./"
        try:
            while True:
                line = input().lower()
                result = ""
                for i in line:
                    if i in keyboard:
                        index = keyboard.index(i)
                        result += keyboard[index - 2]
                    else:
                        result += i
                print(result)
        except EOFError:
            exit()

if __name__ == "__main__":
    Solution()