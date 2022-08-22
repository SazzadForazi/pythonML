import csv
with open('datafile.csv', 'w', newline='') as f:
    data = csv.writer(f)
    data.writerow(['COL1', 'COL2', 'COL3'])
    for i in range(1, 100):
        data.writerow(['one', 'two', 'three'])
