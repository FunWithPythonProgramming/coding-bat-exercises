def phone_numbers(phone):
    num = [int(phone)]

    if len(num) == 10 and num[0] >= 7:
       return "Yes"
    else:
        return "No"
