from datetime import datetime

# 16th July
def days_to_snake_day(from_date=None):
    if from_date is None:
        from_date = datetime.now()

    if from_date.month == 7 and from_date.day == 16:
        return 0

    if from_date.month >= 7 or (from_date.month == 7 and from_date.day >= 16):
        day_of_snake = datetime(from_date.year + 1, 8, 16)
    else:
        day_of_snake = datetime(from_date.year, 8, 16)

    return (day_of_snake - from_date).days