import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):

    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # pass
    formatted_date = datetime.fromisoformat(iso_string.rstrip("Z"))
    return formatted_date.strftime("%A %d %B %Y")

# new_date = convert_date("2021-07-05T07:00:00+08:00")
# print(f"{new_date}")

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celsius, rounded to 1 decimal place.
    """
    #pass

    temp_in_c = (temp_in_fahrenheit - 32) * 5 / 9
    return round(float(temp_in_c),1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # pass
    mean = sum(float(x) for x in weather_data) / len(weather_data)
    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # pass
    import csv
    data = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row:  # skip empty lines
                converted_row = [row[0].strip()] + [int(x.strip()) for x in row[1:]]
                data.append(converted_row)
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # pass
    if not weather_data:
        return ()
    float_data = [float(x) for x in weather_data]
    min_data = min(float_data)
    return min_data, len(float_data) - 1 - float_data[::-1].index(min_data)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # pass
    if not weather_data:
        return ()
    float_data = [float(x) for x in weather_data]
    max_value = max(float_data)
    index = len(float_data) - 1 - float_data[::-1].index(max_value)
    return max_value, index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass
    if not weather_data:
        return "No weather data available.\n"
    
    num_days = len(weather_data)
    
    highs = [convert_f_to_c(float(day[2])) for day in weather_data]
    lows = [convert_f_to_c(float(day[1])) for day in weather_data]


    min_temp, min_index = find_min(lows)
    min_day = convert_date(weather_data[min_index][0])

    min_temp, min_index = find_min(lows)
    min_day = convert_date(weather_data[min_index][0])

    max_temp = max(highs)
    max_index = highs.index(max_temp)
    max_day = convert_date(weather_data[max_index][0])

    avg_high = round(sum(highs) / num_days, 1)
    avg_low = round(sum(lows) / num_days, 1)

    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {min_day}.\n"
        f"  The highest temperature will be {format_temperature(max_temp)}, and will occur on {max_day}.\n"
        f"  The average low this week is {format_temperature(avg_low)}.\n"
        f"  The average high this week is {format_temperature(avg_high)}.\n"
    )

    return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass
    summary_lines = []
    for day in weather_data:
        date = convert_date(day[0])
        min_temp = format_temperature(convert_f_to_c(float(day[1])))
        max_temp = format_temperature(convert_f_to_c(float(day[2])))
        summary_lines.append(
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_temp}\n"
            f"  Maximum Temperature: {max_temp}\n"
            f" \n"
        )

    return "\n".join(summary_lines) + "\n"

# example_one = [
#     ["2021-07-02T07:00:00+08:00", 49, 67],
#     ["2021-07-03T07:00:00+08:00", 57, 68],
#     ["2021-07-04T07:00:00+08:00", 56, 62],
#     ["2021-07-05T07:00:00+08:00", 55, 61],
#     ["2021-07-06T07:00:00+08:00", 53, 62]
# ]
# print (generate_daily_summary(example_one))



