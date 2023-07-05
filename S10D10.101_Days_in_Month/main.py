def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                l_return = True
            else:
                l_return = False
        else:
            l_return = True
    else:
        l_return = False
    return l_return


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month >= 1 and month <= 12:
        if month == 2 and is_leap(year):
            l_return = 29
        else:
            l_return = month_days[month - 1]
    else:
        l_return = 0
    return l_return


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
