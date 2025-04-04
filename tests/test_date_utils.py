# toolbelt/tests/test_date_utils.py

import pytest
from datetime import datetime
from logic.date_utils import calculate_date


def test_calculate_date_days():
    """Test adding days to date."""
    start = datetime(2025, 1, 1)
    result = calculate_date(start, 10, 'Days')
    assert result == datetime(2025, 1, 11)


def test_calculate_date_weeks():
    """Test adding weeks to date."""
    start = datetime(2025, 1, 1)
    result = calculate_date(start, 2, 'Weeks')
    assert result == datetime(2025, 1, 15)


def test_calculate_date_months():
    """Test adding months to date."""
    start = datetime(2025, 1, 1)
    result = calculate_date(start, 2, 'Months')
    assert result == datetime(2025, 3, 1)  


def test_calculate_date_years():
    """Test adding years to date."""
    start = datetime(2025, 1, 1)
    result = calculate_date(start, 2, 'Years')
    assert result == datetime(2027, 1, 1)


def test_invalid_unit():
    """Test that invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        # Passing an alphanumeric character instead of number
        calculate_date(datetime(2024, 1, 1), 'a', 'Days')


def test_calculate_date_leap_year():
    """Test edge cases around leap years."""
    start = datetime(2024, 2, 20)
    # 2024 is a leap year
    day_result = calculate_date(start, 9, 'Days')      # Feb. 29
    week_result = calculate_date(start, 3, 'Weeks')     # Mar. 12
    month_result = calculate_date(start, 2, 'Months')    # Apr. 20
    year_result = calculate_date(start, 1, 'Years')     # Feb. 20, 2025
    assert day_result == datetime(2024, 2, 29)
    assert week_result == datetime(2024, 3, 12)
    assert month_result == datetime(2024, 4, 20)
    assert year_result == datetime(2025, 2, 20)