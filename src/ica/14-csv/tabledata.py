"""
Examples of how to process CSV files

@author: Susan Fox
@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""

from helpers import *

# Example: Representing tabular data as a list of dictionaries
directory = [{'Name': 'Fox, Susan', 'Phone': '6553', 'Building': 'Olin-Rice', 'OfficeNum': '230'},
             {'Name': 'Cranford, James', 'Phone': '2083', 'Building': 'Olin-Rice', 'OfficeNum': '143'},
             {'Name': 'Syed, Una', 'Phone': '1059', 'Building': 'Campus Center', 'OfficeNum': '399'},
             {'Name': 'Thimus, Reg', 'Phone': '9989', 'Building': 'Leonard', 'OfficeNum': '22'},
             {'Name': 'Warner, Elen', 'Phone': '1113', 'Building': 'Old Main', 'OfficeNum': '402'},
             {'Name': 'Best, Fleur', 'Phone': '9281', 'Building': 'Carnegie', 'OfficeNum': '003'},
             {'Name': 'Ryan, Frazer', 'Phone': '1923', 'Building': 'Old Main', 'OfficeNum': '281'},
             {'Name': 'Mueller, Marcel', 'Phone': '9011', 'Building': 'Leonard', 'OfficeNum': '234'},
             {'Name': 'Glover, Stephanie', 'Phone': '2341', 'Building': 'Carnegie', 'OfficeNum': '832'},
             {'Name': 'Glass, Abdullah', 'Phone': '1122', 'Building': '77 Mac', 'OfficeNum': '102'},
             {'Name': 'Petersen, Rosa', 'Phone': '2392', 'Building': 'Olin-Rice', 'OfficeNum': '333'},
             {'Name': 'Mora, Mohamed', 'Phone': '2229', 'Building': 'Campus Center', 'OfficeNum': '012'},
             {'Name': 'Friedman, Maryam', 'Phone': '3142', 'Building': 'Old Main', 'OfficeNum': '194'},
             {'Name': 'Li, Elena', 'Phone': '1923', 'Building': 'Olin-Rice', 'OfficeNum': '119'}]


def lookup_phone(name, direct_table):
    """
    Given a name and a list-of-dictionaries sunTable, look up the person's
    phone number
    """
    for row in direct_table:
        if row['Name'] == name:
            return row['Phone']

    return "No entry: " + name


def collect_by_building(building, table):
    """
    Given the name of a building, and a sunTable, make a list of all
    the entries in the sunTable belonging to that building and return that list
    """
    match_list = []
    for row in table:
        if row['Building'] == building:
            match_list.append(row)

    return match_list


def count_sunsets_before(hour_time, table):
    """
    Takes in the sunTable for the sunrise/sunset data, and counts how many
    rows have a sunset hour that is before the input hour time, which must
    be an integer in 24-hour mode so that 1pm is 13, 6pm is 18, etc.
    It returns the total count.
    """
    count = 0
    for row in table:
        sunset_hr = row['SunSetHour']
        if int(sunset_hr) < hour_time:
            count += 1

    return count


def daylight_hours(rise_hour, rise_min, set_hour, set_min):
    """
    Given four values, the hour and minute of sunrise, and the hour and minute of sunset, this computes the
    number of hours of daylight and returns that value as a floating-point number.
    """
    rise_time = (60 * rise_hour) + rise_min
    set_time = (60 * set_hour) + set_min
    minute_diff = set_time - rise_time
    hour_diff = minute_diff / 60
    return hour_diff


def main():
    print(lookup_phone('Fox, Susan', directory))
    print(lookup_phone('Shoop, Libby', directory))

    field_names, sun_table = read_csv("DataFiles/sunRiseSet.csv")
    print(field_names)
    print(sun_table[0])  # printing just the first row of data
    print_table(sun_table, field_names, 15)

    # may15_data = lookup_by_date('May', 15, sun_table)
    # print(may15_data)
    # oct31_data = lookup_by_date('October', '31', sun_table)
    # print(oct31_data)

    olri = collect_by_building('Olin-Rice', directory)
    print(olri)
    cc = collect_by_building('Campus Center', directory)
    print_table(cc, ['Name', 'Phone', 'Building', 'OfficeNum'])

    # march_data = select_by_month('March', sun_table)
    # july_data = select_by_month('July', sun_table)
    # january_data = select_by_month('January', sun_table)
    # print_table(march_data, field_names, 15)

    print("Sunsets before 6pm =", count_sunsets_before(18, sun_table))
    print("Sunsets before 10pm =", count_sunsets_before(22, sun_table))
    print("Sunsets before 4pm =", count_sunsets_before(16, sun_table))


if __name__ == '__main__':
    main()
