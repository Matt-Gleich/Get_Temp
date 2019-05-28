import datetime


def current_date():
    """
    Get the current date
    :return: string
    """
    tday = str(datetime.datetime.now())
    elements = tday.split(" ")
    date_sections = elements[0]
    return date_sections


# Testing
# print(current_date())


def current_time():
    """
    Get the current time of day
    :return: string
    """
    tday = str(datetime.datetime.now())
    elements = tday.split(" ")
    time_selection = elements[1]
    time_elements = time_selection.split(":")
    hour = int(time_elements[0])
    minute = int(time_elements[1])
    second = float(time_elements[2])
    if hour <= 12:
        morn_night = "AM"
    else:
        morn_night = "PM"
        hour -= 12
    string = "{H}:{M}:{S} {TD}".format(H=str(hour),M=str(minute),S=str(second),TD=str(morn_night))
    return string


# Testing
# print(current_time())