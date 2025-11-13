thonfrom datetime import datetime

def parse_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")