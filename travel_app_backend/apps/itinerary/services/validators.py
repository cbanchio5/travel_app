from datetime import date

class DateValidator:
    @staticmethod
    def validate_arrival_departure(arrival: date, departure: date):
        if arrival >= departure:
            raise ValueError("Departure must be after arrival.")
