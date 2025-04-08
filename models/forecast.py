class Forecast:
    def __init__(self, code: int, condition: str, date: str):
        self.code = code
        self.condition = condition
        self.date = date

    def to_dict(self):
        return {
            "code": self.code,
            "condition": self.condition,
            "date": self.date
        }
