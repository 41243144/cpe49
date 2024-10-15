class Solution:
    def __init__(self) -> None:
        self.main()

    def main(self):
        n = int(input())
        table = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        for _ in range(n):
            month, day = map(int, input().split())
            days = 0
            
            if month < 4:

                for m in range(month, 4):
                    days -= table[m - 1]
                days += day - 4
            elif month > 4:
                for m in range(4, month):
                    days += table[m - 1]
                days += day - 4
            else:
                days = day - 4
            
            result_day = (days % 7 + 7) % 7
            print(days_of_week[result_day])

if __name__ == "__main__":
    Solution()
