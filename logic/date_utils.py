# toolbelt/logic/date_utils.py

from datetime import datetime, timedelta


def add_months(source_date: datetime, months: int) -> datetime:
    """Add months to the date choosen."""
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, (datetime(year, month + 1, 1) - timedelta(days=1)).day)
    return datetime(year, month, day)


def add_years(source_date: datetime, years: int) -> datetime:
    """Add years to the date choosen."""
    try:
        return source_date.replace(year=source_date.year + years)
    except ValueError:
        # Handle leap year
        return source_date.replace(month=2, day=28, year=source_date.year + years)


def calculate_date(start_date: datetime, period: int, unit: str) -> None:
    """Calculates the date given the start date, time period, and time unit to calculate by."""
    if unit == 'Days':
        return start_date + timedelta(days=period)
    elif unit == 'Weeks':
        return start_date + timedelta(weeks=period)
    elif unit == 'Months':
        return add_months(start_date, period)
    elif unit == 'Years':
        return add_years(start_date, period)
    else:
        raise ValueError("Invalid time unit")
