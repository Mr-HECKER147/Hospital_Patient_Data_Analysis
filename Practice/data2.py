import csv

output_file = 'data2.csv'
row_count = 30

with open(output_file, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Calories', 'Duration'])
    writer.writeheader()
    for i in range(row_count):
        calories = 100 + int(round(i * 800.0 / (row_count - 1)))
        duration = 10 + int(round(i * 80.0 / (row_count - 1)))
        writer.writerow({'Calories': calories, 'Duration': duration})

print(f'Generated {row_count} rows in {output_file}')
