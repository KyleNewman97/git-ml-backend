from datetime import datetime

from git_ml_backend.types.date_time import validate_datetime


class TestDateTime:
    def test_validate_datetime_str(self):
        """
        Test that an ISO formatted date time string can be converted to a datetime
        object.
        """
        datetime_str = "2025-02-22 18:42:37+08:00"
        datetime_result = validate_datetime(datetime_str)

        assert isinstance(datetime_result, datetime)

    def test_validate_datetime_datetime(self):
        """
        Test that if a datetime object is passed in then it is simply returned.
        """
        input = datetime.now()
        result = validate_datetime(input)
        assert input == result
