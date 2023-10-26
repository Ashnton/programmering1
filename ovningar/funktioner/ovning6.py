def days_in_month(month):
    monthdict = {
        "January": 31,
        "February": 28,
        "Mars": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    print(monthdict[month])

days_in_month("December")