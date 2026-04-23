all_calculations = ['$10.00 NZD is $12.10 AUD', '$20.00 NZD is $24.20 AUD',
                    '$30.00 NZD is $36.30 AUD', '$40.00 NZD is $48.40 AUD',
                    '$50.00 NZD is $60.50 AUD']

newest_first = list(reversed(all_calculations))

print("=== Oldest to Newest for File ===")
for item in all_calculations:
    print(item)

print()

print("=== Most Recent First ===")
for item in newest_first:
    print(item)
