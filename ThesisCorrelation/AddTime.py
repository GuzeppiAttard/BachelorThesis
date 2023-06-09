import openpyxl

def calculate_total_time(time_values):
    total_minutes = 0
    total_seconds = 0
    total_milliseconds = 0

    for time_str in time_values:
        minutes, seconds, milliseconds = time_str.split('.')
        total_minutes += int(minutes)
        total_seconds += int(seconds)
        total_milliseconds += int(milliseconds)

    # Adjust the time components based on the milliseconds
    total_seconds += total_milliseconds // 1000
    total_milliseconds = total_milliseconds % 1000
    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60

    return "{:01d}.{:02d}.{:02d}".format(total_minutes, total_seconds, total_milliseconds)


# Load the Excel file
filename = 'ThesisResults.xlsx'
wb = openpyxl.load_workbook(filename)
sheet = wb.active

# Get all the time values in column D as a list
time_values = [cell.value for cell in sheet['H'][1:] if cell.value]

# Calculate the total time
total_time = calculate_total_time(time_values)

# Print the total time
print("Total Time:", total_time)
