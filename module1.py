class MyDate:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def get_date_list(cls, string):
        return list(map(int, string.split("-")))

    @staticmethod
    def date_validation(string):
        date_list = MyDate.get_date_list(string)
        return 0 < date_list[0] < 32 and 0 < date_list[1] < 13 and date_list[2] > 0


print(MyDate.get_date_list("14-06-2020"))
print(MyDate.date_validation("0-12-2002"))
print(MyDate("").date_validation("30-03-2050"))
