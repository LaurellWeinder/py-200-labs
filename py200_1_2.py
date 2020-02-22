class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, year, month, day):
        self.__is_valid_date(year, month, day)
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f'{self._year}-{self._month}-{self._day}'

    def __repr__(self):
        return f'Date({self._year}, {self._month}, {self._day})'

    @staticmethod
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False

    @staticmethod
    def get_max_day( year, month):
        leap_year = 1 if Date.is_leap_year(year) else 0
        return Date.DAY_OF_MONTH[leap_year][month - 1]

    @classmethod
    def _days_before_year(cls, year):
        y = year - 1
        return y * 365 + y // 4 - y // 100 + y // 400

    @classmethod
    def _days_before_month(cls, year, month):
        if not 1 <= month <= 12:
            raise ValueError('Month must be in 1...12')
        if month == 2 and cls.is_leap_year(year):
            return 29
        return cls.DAY_OF_MONTH[0][month - 1]

    @property
    def date(self):
        return f'{self._day}.{self._month}.{self._year}'

    @classmethod
    def __is_valid_date(cls, year, month, day):
        if not isinstance(day, int):
            raise TypeError('Year must be int')
        if not isinstance(month, int):
            raise TypeError('Month must be int')
        if not isinstance(year, int):
            raise TypeError('Year must be int')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('Insufficient amount of days for given year and month')
        if not 1 <= month <= 12:
            raise ValueError('Month must be between 1 and 12')

    @date.setter
    def date(self, value):
        value = [int(_) for _ in value.split(',')]
        if len(value) != 3:
            raise ValueError('Invalid date format')
        year, month, day = value
        if self.__is_valid_date(year, month, day):
            self._year = value[0]
            self._month = value[1]
            self._year = value[2]
        else:
            raise ValueError('Invalid date format')

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    def add_year(self, year):
        if not isinstance(year, int):
            raise ValueError
        if int(year) < 0:
            raise ValueError('Year number must be positive')
        self._year += 1

    def add_day(self, day):
        if not isinstance(day, int):
            raise ValueError('Days value must be int')
        if int(day) < 0:
            raise ValueError('Days number must be positive')
        dim = Date.get_max_day(self._year, self._month)
        dbm = dim - self._day
        while day > 0:
            self._day += day
            if self._day > dim:
                self._day = 1
                self._month += 1
                if self._month > 12:
                    self._month = 1
                    self._year += 1
            day -= dim - dbm

    def add_month(self, month):
        if not isinstance(month, int):
            raise ValueError('Months value must be int')
        if int(month) < 0:
            raise ValueError('Months number must be positive')
        if month >= 12:
            self._year += month // 12
            month %= 12
        self._month += month
        if self._month > 12:
            self._year += 1
            self._month %= 12


    @staticmethod
    def date2_date1(date2, date1):
        pass

    @day.setter
    def day(self, value):
        value = int(value)
        self.__is_valid_date(self._year, self._month, value)
        self._day = value

    @month.setter
    def month(self, value):
        value = int(value)
        self.__is_valid_date(self._year, value, self._day)
        self._month = value

    @year.setter
    def year(self, value):
        value = int(value)
        self.__is_valid_date(value, self._month, self._day)
        self._year = value


if __name__ == '__main__':
    date = Date(2020, 12, 14)
    d1 = Date(2019, 1, 11)
    d1.day = 19
    print(d1.month)
    date.add_month(12)
    print(date)
