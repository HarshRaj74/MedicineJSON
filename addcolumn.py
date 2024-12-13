import json
from collections import Counter
from datetime import datetime
import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def add_is_valid_mobile(data):
    for record in data:
        phone_number = record.get("phoneNumber", "")
        is_valid = False

        if phone_number.startswith("+91"):
            phone_number = phone_number[3:]
        elif phone_number.startswith("91"):
            phone_number = phone_number[2:]

        if phone_number.isdigit() and 6000000000 <= int(phone_number) <= 9999999999:
            is_valid = True

        record["isValidMobile"] = is_valid
def validate_phone_numbers(data):
    valid_phone_count = 0

    for record in data:
        phone_number = record.get("phoneNumber", "")
        is_valid = False

        if phone_number.startswith("+91"):
            phone_number = phone_number[3:]
        elif phone_number.startswith("91"):
            phone_number = phone_number[2:]

        if phone_number.isdigit() and 6000000000 <= int(phone_number) <= 9999999999:
            is_valid = True
            valid_phone_count += 1

        record["isValidMobile"] = is_valid

    return valid_phone_count
file_path = '/DataEngineeringQ2.json'
data = load_data(file_path)
valid_phone_count = validate_phone_numbers(data)
print(f"Valid Phone Numbers: {valid_phone_count}")
