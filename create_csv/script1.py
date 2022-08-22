import csv

with open('cs.csv', 'w', newline='') as f:
    fieldnames = ['COL1', 'COL2', 'COL3']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    thewriter.writeheader()
    for i in range(1, 10):
        thewriter.writerow({'COL1': 'one', 'COL2': 'two', 'COL3': 'three'})
        thewriter.writerow({'COL1': 'four', 'COL2': 'five', 'COL3': 'six'})
