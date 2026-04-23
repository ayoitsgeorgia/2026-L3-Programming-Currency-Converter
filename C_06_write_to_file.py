from datetime import date

calculations = ['$10.00 NZD is $12.10 AUD', '$20.00 NZD is $24.20 AUD',
                '$30.00 NZD is $36.30 AUD', '$40.00 NZD is $48.40 AUD',
                '$50.00 NZD is $60.50 AUD']

# **** Get current date for heading and filename ****
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"Currency_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:
    text_file.write("***** Currency Calculations *****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to newest)...\n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")
