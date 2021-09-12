# Use the Calendar module to get the day of the week from a date entered as MM DD YYYY from STDIN
# Get numerical day of week from calendar.weekday (0-6), and use that number to access index of calendar.day_name()
import calendar

if __name__ == '__main__':
    mon, day, year = map(int, input().split())
    print((calendar.day_name[calendar.weekday(year, mon, day)]).upper())
