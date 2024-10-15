class Solution():
    def __init__(self) -> None:
        self.main()

    def main(self):
        n = int(input())
        finger_map = {
            'c': [2, 3, 4, 7, 8, 9, 10],
            'd': [2, 3, 4, 7, 8, 9],
            'e': [2, 3, 4, 7, 8],
            'f': [2, 3, 4, 7],
            'g': [2, 3, 4],
            'a': [2, 3],
            'b': [2],
            'C': [3],
            'D': [1, 2, 3, 4, 7, 8, 9],
            'E': [1, 2, 3, 4, 7, 8],
            'F': [1, 2, 3, 4, 7],
            'G': [1, 2, 3, 4],
            'A': [1, 2, 3],
            'B': [1, 2]
        }

        while n:
            n -= 1

            finger_press = [False for _ in range(10)]
            finger_press_map = [0 for _ in range(10)]

            line = input()

            for ch in line:
                if ch in finger_map:
                    for index in range(10):
                        if index + 1 in finger_map[ch] and not finger_press[index]:
                            finger_press[index] = True
                            finger_press_map[index] += 1
                            
                        elif index + 1 not in finger_map[ch]:
                            finger_press[index] = False
            
            print(" ".join(map(str, finger_press_map)))




if __name__ == "__main__":
    Solution()